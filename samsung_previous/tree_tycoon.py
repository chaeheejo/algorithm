N, M = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(M)]

supplement = [[0]*N for _ in range(N)]
supplement[-1][0], supplement[-1][1], supplement[-2][0], supplement[-2][1] = 1,1,1,1

dxy=[(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
for m in range(M):
    d,p = cmd[m][0]-1,cmd[m][1]

    move_supplement=[[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if supplement[i][j]==1:
                nx,ny = (i+dxy[d][0]*p)%N, (j+dxy[d][1]*p)%N
                move_supplement[nx][ny]=1
                tree[nx][ny]+=1
    supplement = move_supplement

    for i in range(N):
        for j in range(N):
            if supplement[i][j]==1:
                neighbor = 0
                for k in range(1,9,2):
                    nx,ny = i+dxy[k][0], j+dxy[k][1]
                    if 0<=nx<N and 0<=ny<N and tree[nx][ny]>0:
                        neighbor+=1
                tree[i][j]+=neighbor

    buy_supplement = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if supplement[i][j]==1:
                continue
            if tree[i][j]>1:
                tree[i][j]-=2
                buy_supplement[i][j]=1
    supplement = buy_supplement

answer=0
for t in tree:
    answer+=sum(t)
print(answer)