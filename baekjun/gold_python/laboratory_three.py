N, M = map(int, input().split())
virus_map = [list(map(int, input().split())) for _ in range(N)]

virus=[]
wall=[]
for i in range(N):
    for j in range(N):
        if virus_map[i][j]==1:
            wall.append((i,j))
        elif virus_map[i][j]==2:
            virus.append((i, j))

def comb(arr, num):
    for i in range(len(arr)):
        if num==1:
            yield [arr[i]]
        else:
            for next in comb(arr[i+1:], num-1):
                yield [arr[i]]+next

activate_virus_index=[]
virus_num=len(virus)
for i in comb(range(virus_num), M):
    activate_virus_index.append(i)

answer=9999
xdirect = [-1,1,0,0]
ydirect = [0,0,-1,1]
for activate in activate_virus_index:
    visited = [[-1] * N for _ in range(N)]
    queue=[]
    cnt=0

    for a in activate:
        i, j = virus[a]
        visited[i][j]=0
        queue.append((i,j))
    for w in wall:
        i, j = w
        visited[i][j]=0

    cur=0
    while cur<len(queue):
        i, j = queue[cur]
        cur+=1

        for k in range(4):
            tmpI, tmpJ = i+xdirect[k], j+ydirect[k]
            if 0<=tmpI<N and 0<=tmpJ<N and visited[tmpI][tmpJ]==-1 :
                queue.append((tmpI, tmpJ))
                visited[tmpI][tmpJ]=visited[i][j]+1
                if virus_map[tmpI][tmpJ]==0:
                    cnt = visited[tmpI][tmpJ]
    solved=True
    for i in range(N):
        if visited[i].count(-1):
            solved=False
            break
    if solved:
        answer = min(answer, cnt)

if answer==9999:
    print(-1)
else:
    print(answer)