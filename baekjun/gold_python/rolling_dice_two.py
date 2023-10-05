N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dice_updown = [6,2,1,5]
dice_leftright = [6,4,1,3]
dxy = [(0,1),(1,0),(0,-1),(-1,0)]
def dice_move(i,j,d):
    global dice_leftright,dice_updown

    nx,ny = i+dxy[d][0], j+dxy[d][1]
    if 0>nx or nx>=N or 0>ny or ny>=M:
        d = (d+2)%4
        nx, ny = i+dxy[d][0], j+dxy[d][1]

    if d==0:
        new=[0]*4
        for n in range(4):
            new[n] = dice_leftright[(n-1)%4]
        dice_leftright = new
        dice_updown[0], dice_updown[2] = dice_leftright[0], dice_leftright[2]
    elif d==2:
        new = [0]*4
        for n in range(4):
            new[n] = dice_leftright[(n+1)%4]
        dice_leftright = new
        dice_updown[0], dice_updown[2] = dice_leftright[0], dice_leftright[2]
    elif d==1:
        new = [0] * 4
        for n in range(4):
            new[n] = dice_updown[(n-1)%4]
        dice_updown = new
        dice_leftright[0], dice_leftright[2] = dice_updown[0], dice_updown[2]
    elif d==3:
        new = [0] * 4
        for n in range(4):
            new[n] = dice_updown[(n+1)%4]
        dice_updown = new
        dice_leftright[0], dice_leftright[2] = dice_updown[0], dice_updown[2]

    if dice_updown[0] > board[nx][ny]:
        d = (d+1)%4
    elif dice_updown[0] < board[nx][ny]:
        d = (d-1)%4

    return nx,ny,d

def count_num(i,j):
    queue = [(i,j)]
    cur=0
    visited[i][j]=1

    while cur<len(queue):
        x,y = queue[cur]
        cur+=1

        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
                if board[i][j]==board[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny]=1

    return len(queue)

answer=0
i,j,d=0,0,0
for _ in range(K):
    i,j,d = dice_move(i,j,d)

    visited = [[0]*M for _ in range(N)]
    n = count_num(i,j)
    answer += (board[i][j] * n)

print(answer)