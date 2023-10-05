N, M, K =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

smell = [[[0,0]]*N for _ in range(N)]

def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1]>0:
                smell[i][j][1]-=1
            if board[i][j]>0:
                smell[i][j] = [board[i][j], K]

dxy = [(-1,0),(1,0),(0,-1),(0,1)]
def move_shark():
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            flag=0
            if board[i][j]>0:
                shark_num = board[i][j]-1
                d = direction[shark_num]-1
                for k in range(4):
                    p = priority[shark_num][d][k]-1
                    nx,ny = i+dxy[p][0], j+dxy[p][1]
                    if 0<=nx<N and 0<=ny<N and smell[nx][ny][1]==0:
                        if new_board[nx][ny]==0:
                            new_board[nx][ny]=board[i][j]
                        else:
                            new_board[nx][ny] = min(new_board[nx][ny],board[i][j])
                        direction[shark_num]=p+1
                        flag=1
                        break
                if flag==0:
                    for k in range(4):
                        p = priority[shark_num][d][k]-1
                        nx,ny = i+dxy[p][0], j+dxy[p][1]
                        if 0<=nx<N and 0<=ny<N and smell[nx][ny][0]==board[i][j]:
                            direction[shark_num] = p+1
                            new_board[nx][ny] = board[i][j]
                            break
    return new_board

answer=0
for _ in range(1001):
    update_smell()
    board = move_shark()

    answer+=1
    flag=0
    for i in range(N):
        for j in range(N):
            if board[i][j]>1:
                flag=1

    if flag==0:
        print(answer)
        break
    if answer>=1000:
        print(-1)
        break