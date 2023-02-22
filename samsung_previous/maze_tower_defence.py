N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [list(map(int, input().split())) for _ in range(M)]

dxy = [(0,1),(1,0),(0,-1),(-1,0)]
idx,i,j,d=[],0,0,0
visited = [[0]*N for _ in range(N)]
visited[0][0]=1
while True:
    if i==N//2 and j==N//2:
        break
    idx.append([i,j])
    x,y = i+dxy[d][0], j+dxy[d][1]
    if x<0 or x>=N or y<0 or y>=N or visited[x][y]==1:
        d = (d+1)%4
        x,y = i+dxy[d][0],j+dxy[d][1]
    i,j = x,y
    visited[i][j]=1

def arrange_maze():
    cur=len(idx)-1
    blank=0
    while cur>-1:
        x,y = idx[cur]
        if board[x][y]==0:
            blank+=1
        else:
            if blank>0:
                past_x,past_y = idx[cur+blank]
                board[past_x][past_y] = board[x][y]
                board[x][y] = 0
        cur-=1

def kill_monster():
    cur = len(idx) - 2
    past, same = board[idx[-1][0]][idx[-1][1]], [idx[cur+1]]
    rtn=0
    while cur>-1:
        x,y = idx[cur]
        if past!=board[x][y]:
            if len(same)>=4:
                for nx,ny in same:
                    rtn+=board[nx][ny]
                    board[nx][ny]=0
            past=board[x][y]
            same=[[x,y]]
        else:
            same.append([x,y])
        cur-=1
    return rtn

def new_maze():
    new_monster = []
    cur = len(idx)-2
    past,cnt=board[idx[-1][0]][idx[-1][1]],1
    while cur>-1:
        x,y = idx[cur]
        if past!=board[x][y]:
            new_monster.extend([cnt,past])
            past=board[x][y]
            cnt=1
        else:
            cnt+=1
        if board[x][y]==0 :
            break
        cur-=1

    new_board = [[0]*N for _ in range(N)]
    cur = len(idx) - 1
    for m in new_monster:
        x,y = idx[cur]
        new_board[x][y]=m
        cur-=1
        if cur<0:
            break
    return new_board

score=0
for m in range(M):
    D,P = dp[m]

    attack_i,attack_j = N//2,N//2
    for _ in range(P):
        attack_i,attack_j = attack_i+dxy[D][0], attack_j+dxy[D][1]
        score+=board[attack_i][attack_j]
        board[attack_i][attack_j] = 0

    arrange_maze()

    while True:
        tmp = kill_monster()
        if tmp==0:
            break
        score+=tmp
        arrange_maze()
    board = new_maze()

print(score)