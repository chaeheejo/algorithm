N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]

board = [[[] for _ in range(N)] for _ in range(N)]
horse = []
for k in range(K):
    x,y,d = map(int, input().split())
    if d==4:
        d=2
    elif d==2:
        d=3
    elif d==3:
        d=4
    horse.append([x-1,y-1,d-1])
    board[x-1][y-1].append(k)

def move_white(nx,ny,k):
    x,y,_ = horse[k]

    idx = board[x][y].index(k)
    for nxt in board[x][y][idx:]:
        horse[nxt][0],horse[nxt][1] = nx,ny

    board[nx][ny].extend(board[x][y][idx:])
    board[x][y] = board[x][y][:idx]


def move_red(nx,ny,k):
    x,y,_ = horse[k]
    idx = board[x][y].index(k)
    for nxt in board[x][y][idx:]:
        horse[nxt][0],horse[nxt][1] = nx,ny

    opposite = board[x][y][idx:]
    for i in range(len(opposite)-1,-1,-1):
        board[nx][ny].append(opposite[i])

    board[x][y] = board[x][y][:idx]

def move_blue(k):
    horse[k][2] = (horse[k][2]+2)%4
    x,y,d = horse[k]
    nx,ny = x+dxy[d][0],y+dxy[d][1]
    if 0<=nx<N and 0<=ny<N:
        if color[nx][ny]==0:
            move_white(nx,ny,k)
        elif color[nx][ny]==1:
            move_red(nx,ny,k)

def check_finish():
    for i in range(N):
        for j in range(N):
            if len(board[i][j])>3:
                return True
    return False

answer=0
dxy = [(0,1),(1,0),(0,-1),(-1,0)]
while True:
    answer+=1
    flag=0
    for k in range(K):
        x,y,d = horse[k]
        nx,ny = x+dxy[d][0], y+dxy[d][1]
        if 0<=nx<N and 0<=ny<N:
            if color[nx][ny]==0:
                move_white(nx,ny,k)
            elif color[nx][ny]==1:
                move_red(nx,ny,k)
            else:
                move_blue(k)
        else:
            move_blue(k)
        if check_finish():
            flag=1
            break
    if flag:
        break
    if answer>1000:
        answer=-1
        break
print(answer)