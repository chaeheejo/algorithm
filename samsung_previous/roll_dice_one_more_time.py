N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def move_dice(d):
    global dice_side,dice_up
    if d==0:
        tmp = dice_side.pop(0)
        dice_side.append(tmp)
        dice_up[1], dice_up[-1] = dice_side[1], dice_side[-1]
    elif d==1:
        tmp = dice_up.pop(0)
        dice_up.append(tmp)
        dice_side[1], dice_side[-1] = dice_up[1], dice_up[-1]
    elif d==2:
        tmp = dice_side.pop()
        dice_side.insert(0,tmp)
        dice_up[1], dice_up[-1] = dice_side[1], dice_side[-1]
    else:
        tmp = dice_up.pop()
        dice_up.insert(0,tmp)
        dice_side[1], dice_side[-1] = dice_up[1], dice_up[-1]

def get_score(i,j):
    queue=[[i,j]]
    cur=0
    visited=[[0]*N for _ in range(N)]
    visited[i][j]=1
    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and board[nx][ny]==board[i][j]:
                queue.append([nx,ny])
                visited[nx][ny]=1
    return len(queue)*board[i][j]

dice_up = [5,6,2,1]
dice_side = [4,6,3,1]
dxy = [(0,1),(1,0),(0,-1),(-1,0)]
di, dj, d, score = 0, 0, 0, 0
for _ in range(M):
    nx, ny = di + dxy[d][0], dj + dxy[d][1]
    if nx<0 or nx>=N or ny<0 or ny>=N:
        d = (d+2)%4
        nx,ny = di + dxy[d][0], dj+dxy[d][1]
    di,dj = nx,ny

    move_dice(d)
    score+=get_score(di, dj)

    if dice_up[1]>board[di][dj]:
        d = (d+1)%4
    elif dice_up[1]<board[di][dj]:
        d = (d-1)%4

print(score)