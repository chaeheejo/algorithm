N, M, X, Y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

def move(c):
    global dice_leftright, dice_updown

    if c==1:
        new = [dice_leftright[-1]]
        for i in range(3):
            new.append(dice_leftright[i])
        dice_leftright = new
    elif c==2:
        new = []
        for i in range(1,4):
            new.append(dice_leftright[i])
        new.append(dice_leftright[0])
        dice_leftright = new
    elif c==3:
        new = []
        for i in range(1, 4):
            new.append(dice_updown[i])
        new.append(dice_updown[0])
        dice_updown = new
    elif c==4:
        new = [dice_updown[-1]]
        for i in range(3):
            new.append(dice_updown[i])
        dice_updown = new

    if c==1 or c==2:
        dice_updown[0] = dice_leftright[0]
        dice_updown[2] = dice_leftright[2]
    else:
        dice_leftright[0] = dice_updown[0]
        dice_leftright[2] = dice_updown[2]

dice_updown = [0,0,0,0]
dice_leftright = [0,0,0,0]
dxy = [(0,1),(0,-1),(-1,0),(1,0)]
x, y = X,Y
for k in range(K):
    c= cmd[k]

    nx, ny = x+dxy[c-1][0], y+dxy[c-1][1]
    if 0<=nx<N and 0<=ny<M:
        move(c)

        if board[nx][ny]==0:
            board[nx][ny] = dice_updown[0]
        else:
            dice_updown[0] = board[nx][ny]
            dice_leftright[0] = board[nx][ny]
            board[nx][ny]=0
        x, y = nx, ny

        print(dice_updown[2])