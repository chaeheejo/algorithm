N, M, K = map(int, input().split())
board=[list(map(int, input().split())) for _ in range(N)]

air,office = [],[]
for i in range(N):
    for j in range(N):
        if board[i][j]==0:
            continue
        elif board[i][j]==1:
            office.append([i,j])
        else:
            air.append([i,j,(board[i][j]-1)%4])

board = [[0]*N for _ in range(N)]

wall=[[0]*N for _ in range(N)]
for _ in range(M):
    x,y,s = map(int, input().split())
    if s==0:
        wall[x-1][y-1] += 1
    else:
        wall[x-1][y-1] += 10

def check_wall(x,y,d):
    nx,ny = x+dxy[d][0], y+dxy[d][1]
    if 0<=nx<N and 0<=ny<N:
        if d==0:
            if wall[nx][ny]%2!=1:
                return True
        elif d==1:
            if wall[x][y]<10:
                return True
        elif d==2:
            if wall[x][y]%2!=1:
                return True
        else:
            if wall[nx][ny]<10:
                return True
    return False

def spread_air(i,j,ad):
    queue=[[i,j,5]]
    cur=0
    visited=[[0]*N for _ in range(N)]
    visited[i][j]=1

    while cur<len(queue):
        x,y,air = queue[cur]
        cur+=1
        spread_board[x][y]+=air

        for k in range(-1,2):
            d = (ad+k)%4
            if check_wall(x,y,d):
                nx, ny = x+dxy[d][0], y+dxy[d][1]
                if k==0:
                    if visited[nx][ny]==0 and air-1>0:
                        queue.append([nx,ny,air-1])
                    visited[nx][ny]=1
                else:
                    if check_wall(nx,ny,ad):
                        dx, dy = nx+dxy[ad][0], ny+dxy[ad][1]
                        if visited[dx][dy]==0 and air-1>0:
                            queue.append([dx,dy,air-1])
                        visited[dx][dy]=1

def mix_air():
    mix_board = [b[:] for b in board]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if check_wall(i,j,k):
                    nx,ny = i+dxy[k][0],j+dxy[k][1]
                    diff = abs(board[i][j]-board[nx][ny])//4
                    if board[i][j]<board[nx][ny]:
                        mix_board[i][j] = mix_board[i][j]+diff
                    elif board[i][j]>board[nx][ny]:
                        mix_board[i][j] = max(0,mix_board[i][j]-diff)
    return mix_board

def decline_border():
    for i in range(N):
        for j in range(N):
            if i==0 or i==N-1:
                if board[i][j]>0:
                    board[i][j]-=1
            else:
                if j==0 or j==N-1:
                    if board[i][j]>0:
                        board[i][j]-=1

dxy = [(1,0),(0,-1),(-1,0),(0,1)]
spread_board = [[0] * N for _ in range(N)]
for x,y,d in air:
    spread_air(x+dxy[d][0],y+dxy[d][1],d)

answer=0
while True:
    for i in range(N):
        for j in range(N):
            board[i][j]+=spread_board[i][j]

    board = mix_air()
    decline_border()
    answer+=1

    flag=1
    for x,y in office:
        if board[x][y]<K:
            flag=0
    if flag==1:
        break
    if answer>100:
        answer=-1
        break

print(answer)