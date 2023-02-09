N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def grow():
    grow_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                neighbor = 0
                for k in range(4):
                    nx, ny = i + dxy[k][0], j + dxy[k][1]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                        neighbor += 1
                grow_board[i][j] = board[i][j] + neighbor
            else:
                grow_board[i][j] = board[i][j]
    return grow_board

def spread():
    spread_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                blank = []
                for k in range(4):
                    nx, ny = i + dxy[k][0], j + dxy[k][1]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                        blank.append([nx, ny])
                if len(blank) > 0:
                    spread_value = board[i][j] // len(blank)
                    for x, y in blank:
                        spread_board[x][y] += spread_value
                spread_board[i][j] = board[i][j]
            elif board[i][j] <= -1:
                spread_board[i][j] = board[i][j]
    return spread_board

sdxy = [(1,1),(-1,1),(-1,-1),(1,-1)]
def kill(i, j):
    die=board[i][j]
    for k in range(4):
        nx,ny = i+sdxy[k][0], j+sdxy[k][1]
        for _ in range(K):
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==0 or board[nx][ny]<=-1:
                    break
                else:
                    die += board[nx][ny]
                    nx += sdxy[k][0]
                    ny += sdxy[k][1]
            else:
                break
    return die

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer=0
for _ in range(M):
    board = grow()
    board = spread()

    for i in range(N):
        for j in range(N):
            if board[i][j]<-1:
                board[i][j]+=100

    max_tree = -1
    die_tree=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]>0:
                die_tree[i][j] = kill(i, j)
                max_tree = max(max_tree,die_tree[i][j])

    if max_tree==-1:
        continue

    candidate=[]
    for i in range(N):
        for j in range(N):
            if max_tree==die_tree[i][j]:
                candidate.append([i,j])
    candidate.sort(key=lambda x:(x[0],x[1]))

    die_i,die_j = candidate[0][0],candidate[0][1]

    answer += board[die_i][die_j]

    board[die_i][die_j] = C*(-100)
    for k in range(4):
        nx, ny = die_i+sdxy[k][0], die_j+sdxy[k][1]
        for _ in range(K):
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==0 or board[nx][ny]<-1:
                    board[nx][ny] = C*(-100)
                    break
                elif board[nx][ny]==-1:
                    break
                else:
                    answer += board[nx][ny]
                    board[nx][ny] = C*(-100)
                    nx += sdxy[k][0]
                    ny += sdxy[k][1]
            else:
                break

print(answer)