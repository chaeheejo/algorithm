M, N, H = map(int, input().split())
tomatoes = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

queue = []
cur=0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoes[h][i][j]==1:
                queue.append((h,i,j))

dxy = [(1,0),(-1,0),(0,1),(0,-1)]
def ripen():
    global cur
    while cur<len(queue):
        cur_h,cur_i,cur_j = queue[cur]
        cur+=1

        if cur_h-1 >= 0 and tomatoes[cur_h-1][cur_i][cur_j]==0:
            tomatoes[cur_h-1][cur_i][cur_j]=tomatoes[cur_h][cur_i][cur_j]+1
            queue.append((cur_h-1,cur_i,cur_j))
        if cur_h+1<H and tomatoes[cur_h+1][cur_i][cur_j]==0:
            tomatoes[cur_h+1][cur_i][cur_j] = tomatoes[cur_h][cur_i][cur_j]+1
            queue.append((cur_h+1,cur_i,cur_j))

        for k in range(4):
            ni = cur_i + dxy[k][0]
            nj = cur_j + dxy[k][1]

            if 0<=ni<N and 0<=nj<M and tomatoes[cur_h][ni][nj]==0:
                tomatoes[cur_h][ni][nj]=tomatoes[cur_h][cur_i][cur_j]+1
                queue.append((cur_h, ni, nj))

ripen()

flag=0
answer=0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoes[h][i][j]==0:
                flag=1
                break
            answer = max(answer, tomatoes[h][i][j])
        if flag:
            break
    if flag:
        break

if flag:
    print(-1)
else:
    print(answer-1)