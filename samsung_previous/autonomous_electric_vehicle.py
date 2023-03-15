N, M, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            board[i][j]=-1

x, y = map(int, input().split())
car_x,car_y = x-1,y-1
psn_dst = [[]]
for m in range(M):
    sx,sy,dx,dy = map(int, input().split())
    board[sx-1][sy-1] = m+1
    psn_dst.append([dx-1, dy-1])

dxy = [(-1,0),(0,-1),(0,1),(1,0)]
def find_passenger():
    queue=[[car_x,car_y,0]]
    cur=0
    visited=[[0]*N for _ in range(N)]
    visited[car_x][car_y]=1
    candidate,min_gas=[],99
    while cur<len(queue):
        x,y,gas = queue[cur]
        cur+=1
        if board[x][y]>0 and gas<=min_gas:
            min_gas=gas
            candidate.append([x,y,gas,board[x][y]])
        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]>-1:
                    queue.append([nx,ny,gas+1])
                visited[nx][ny]=1
    if len(candidate)==0:
        return -1,-1,-1,-1
    candidate.sort(key=lambda x:(x[2],x[0],x[1]))
    return candidate[0]

def move_dest(dx,dy):
    queue=[[car_x,car_y,0]]
    cur=0
    visited = [[0]*N for _ in range(N)]
    visited[car_x][car_y] = 1
    while cur<len(queue):
        x,y,gas = queue[cur]
        cur+=1
        if x==dx and y==dy:
            return gas
        for k in range(4):
            nx,ny = x+dxy[k][0],y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]>-1:
                    queue.append([nx,ny,gas+1])
                visited[nx][ny]=1
    return -1

answer=0
for _ in range(M):
    sx,sy,gas,psn = find_passenger()
    if gas==-1 or C-gas<=0:
        answer=-1
        break
    board[sx][sy]=0
    car_x,car_y=sx,sy
    C-=gas

    dx,dy = psn_dst[psn]
    gas = move_dest(dx,dy)
    if gas==-1 or C-gas<0:
        answer=-1
        break
    car_x,car_y =dx,dy
    C+=gas

if answer==0:
    answer=C
print(answer)