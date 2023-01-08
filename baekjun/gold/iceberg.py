N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

ice = []
for i in range(N):
    for j in range(M):
        if iceberg[i][j]>0:
            ice.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def after_one_year(iceberg, temp_ice):
    temp_iceberg = [item[:] for item in iceberg]
    for i, j in temp_ice:

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if iceberg[nx][ny]<=0:
                temp_iceberg[i][j] -= 1

        if (i,j) in ice and temp_iceberg[i][j]<=0:
            ice.remove((i,j))
    return temp_iceberg

def count_block():
    queue = [(ice[0][0], ice[0][1])]
    visited = [[0]*M for _ in range(N)]
    cur=0

    while cur < len(queue):
        i, j = queue[cur]
        visited[i][j]=1
        cur+=1

        for k in range(4):
            nx = i+ dx[k]
            ny = j+ dy[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if iceberg[nx][ny]>0 and visited[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny]=1

    if len(queue)!=len(ice):
        return True
    else:
        return False

answer=0
while True:
    if count_block()==True:
        break

    iceberg = after_one_year(iceberg, ice[:])
    answer+=1

    if len(ice)==0:
        break

print(answer)