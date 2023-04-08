N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j]==-1:
            board[i][j]=-99

def grow_tree():
    global board
    new_board = [b[:] for b in board]
    dxy = [(-1,0),(0,1),(1,0),(0,-1)]
    for i in range(N):
        for j in range(N):
            if board[i][j]>0:
                for k in range(4):
                    nx,ny = i+dxy[k][0], j+dxy[k][1]
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]>0:
                        new_board[i][j]+=1
    board = new_board

def spread_tree():
    global board
    new_board = [b[:] for b in board]
    dxy = [(-1,0),(0,1),(1,0),(0,-1)]
    for i in range(N):
        for j in range(N):
            if board[i][j]>0:
                neighbor=[]
                for k in range(4):
                    nx,ny = i+dxy[k][0],j+dxy[k][1]
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
                        neighbor.append([nx,ny])
                for nx,ny in neighbor:
                    new_board[nx][ny]+=board[i][j]//len(neighbor)
    board = new_board

def how_many_trees_can_kill(i,j):
    dxy = [(-1,1),(1,1),(1,-1),(-1,-1)]
    rtn=board[i][j]
    for k in range(4):
        nx, ny = i, j
        for _ in range(K):
            nx,ny = nx+dxy[k][0],ny+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]>0:
                rtn+=board[nx][ny]
            else:
                break
    return rtn

def kill_tree(i,j):
    dxy = [(-1,1),(1,1),(1,-1),(-1,-1)]
    board[i][j]=-1*(C+1)
    for k in range(4):
        nx,ny = i,j
        for _ in range(K):
            nx,ny = nx+dxy[k][0],ny+dxy[k][1]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==-99:
                    break
                if board[nx][ny]<=0:
                    board[nx][ny]=-1*(C+1)
                    break
                else:
                    board[nx][ny]=-1*(C+1)

answer=0
for m in range(M):
    grow_tree()
    spread_tree()

    candidate=[]
    for i in range(N):
        for j in range(N):
            if board[i][j]>0:
                candidate.append([how_many_trees_can_kill(i,j),i,j])
    candidate.sort(key=lambda x:(-x[0],x[1],x[2]))

    if len(candidate)>0:
        kill_tree(candidate[0][1],candidate[0][2])
        answer+=candidate[0][0]

    for i in range(N):
        for j in range(N):
            if board[i][j]==-99:
                continue
            elif board[i][j]<0:
                board[i][j]+=1
print(answer)