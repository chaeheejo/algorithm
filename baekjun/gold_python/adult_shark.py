N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

smell = [[[0,0]]*N for _ in range(N)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1]>0:
                smell[i][j][1]-=1
            if board[i][j]!=0:
                smell[i][j] = [board[i][j],K]

def move_shark():
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]!=0:
                d = direction[board[i][j]-1]
                flag=0
                for idx in priority[board[i][j]-1][d-1]:
                    nx,ny = i+dxy[idx-1][0], j+dxy[idx-1][1]
                    if 0<=nx<N and 0<=ny<N:
                        if smell[nx][ny][1]==0:
                            direction[board[i][j]-1]=idx
                            if new_board[nx][ny]==0:
                                new_board[nx][ny]=board[i][j]
                            else:
                                new_board[nx][ny] = min(board[i][j], new_board[nx][ny])
                            flag=1
                            break
                if flag:
                    continue
                for idx in priority[board[i][j]-1][d-1]:
                    nx,ny = i+dxy[idx-1][0], j+dxy[idx-1][1]
                    if 0<=nx<N and 0<=ny<N:
                        if smell[nx][ny][0] == board[i][j]:
                            direction[board[i][j]-1]=idx
                            new_board[nx][ny]=board[i][j]
                            break
    return new_board

answer=0
for _ in range(1001):
    update_smell()
    board = move_shark()
    answer+=1

    flag=1
    for i in range(N):
        for j in range(N):
            if board[i][j]>1:
                flag=0
    if flag:
        print(answer)
        break

    if answer>=1000:
        print(-1)
        break