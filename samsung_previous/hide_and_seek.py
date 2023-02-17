N, M, H, K = map(int, input().split())
runner_xy=[]
runner_d=[]
for _ in range(M):
    i,j,d = map(int, input().split())
    runner_xy.append([i - 1, j - 1])
    runner_d.append(d)

tree = [[0] * N for _ in range(N)]
for _ in range(H):
    i,j = map(int, input().split())
    tree[i-1][j-1] = 1

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = []
i,j=N//2,N//2
go,turn,flag,d=0,1,0,0
while True:
    i,j = i+dxy[d][0], j+dxy[d][1]
    if i==0 and j==0:
        break
    go+=1
    if go==turn:
        if flag==0:
            go,flag=0,1
        else:
            go,flag=0,0
            turn+=1
        d=(d+1)%4
    direction.append([i,j,d])
i,j,d = 0,0,2
visited=[[0]*N for _ in range(N)]
while True:
    if i==N//2 and j==N//2:
        break
    x,y = i+dxy[d][0],j+dxy[d][1]
    if x<0 or x>=N or y<0 or y>=N or visited[x][y]==1:
        d = (d-1)%4
        x, y = i + dxy[d][0], j + dxy[d][1]
    direction.append([i,j,d])
    visited[i][j] = 1
    i,j = x,y
direction.append([N//2,N//2,0])

answer,r=0,0
catcher_i,catcher_j = N//2,N//2
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for k in range(K):

    for m in range(M):
        ri,rj= runner_xy[m]
        if ri==-1:
            continue
        elif abs(catcher_i-ri)+abs(catcher_j-rj)>3:
            continue
        rd = runner_d[m]
        nx,ny = ri + dxy[rd][0], rj + dxy[rd][1]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            rd = (rd+2)%4
            nx,ny = ri + dxy[rd][0], rj + dxy[rd][1]
        if nx==catcher_i and ny==catcher_j:
            continue
        runner_xy[m] = [nx, ny]
        runner_d[m] = rd

    catcher_i,catcher_j = direction[r][0], direction[r][1]
    d = direction[r][2]
    r = (r+1)%(len(direction))

    catch=0
    if tree[catcher_i][catcher_j]==0:
        while [catcher_i,catcher_j] in runner_xy:
            die_idx = runner_xy.index([catcher_i,catcher_j])
            runner_xy[die_idx] = [-1,-1]
            catch+=1

    sight_i, sight_j = catcher_i,catcher_j
    for _ in range(2):
        sight_i,sight_j = sight_i + dxy[d][0], sight_j + dxy[d][1]
        if sight_i<0 or sight_i>=N or sight_j<0 or sight_j>=N:
            continue
        if tree[sight_i][sight_j]==1:
            continue
        while [sight_i,sight_j] in runner_xy:
            die_idx = runner_xy.index([sight_i,sight_j])
            runner_xy[die_idx] = [-1,-1]
            catch+=1

    answer+=(k+1)*catch

print(answer)