N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

hospital = []
for i in range(N):
    for j in range(N):
        if board[i][j]==2:
            hospital.append([i,j])
            board[i][j]=0
        elif board[i][j]==1:
            board[i][j]=-1

def combination(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for nxt in combination(array[i+1:],r-1):
                yield [array[i]]+nxt

dxy = [(-1,0),(0,1),(1,0),(0,-1)]
def spread_vaccine(i,j):
    queue=[[i,j]]
    cur=0
    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        for k in range(4):
            nx,ny = x+dxy[k][0],y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if spread_board[nx][ny]>0:
                    spread_board[nx][ny] = min(spread_board[nx][ny],spread_board[x][y]+1)
                    queue.append([nx,ny])
                elif spread_board[nx][ny]==0:
                    spread_board[nx][ny]=spread_board[x][y]+1
                    queue.append([nx,ny])
                visited[nx][ny]=1

answer=9999
for com in combination(range(len(hospital)),M):
    spread_board = [b[:] for b in board]
    for idx in com:
        x,y = hospital[idx]
        visited = [[0]*N for _ in range(N)]
        visited[x][y]=1
        spread_board[x][y]=0
        spread_vaccine(x,y)
    flag,cur_time=0,0
    for i in range(N):
        for j in range(N):
            if [i,j] in hospital:
                continue
            if spread_board[i][j]==0:
                flag=1
            cur_time = max(cur_time,spread_board[i][j])
    if flag==0:
        answer = min(answer,cur_time)
if answer==9999:
    answer=-1
print(answer)