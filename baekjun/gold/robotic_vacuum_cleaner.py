N, M = map(int, input().split())
R, C, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            visited[i][j]=2

dxy = [(-1,0), (0,1), (1,0), (0,-1)]
def move_vacuum():
    queue = [(R,C,D)]
    cur=0
    visited[R][C]=1

    while cur<len(queue):
        i, j, d = queue[cur]
        nd = d
        cur+=1
        flag=0

        for k in range(4):
            nd -= 1
            nx = i + dxy[nd%4][0]
            ny = j + dxy[nd%4][1]

            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if visited[nx][ny]==0:
                visited[nx][ny]=1
                queue.append((nx, ny, nd%4))
                flag=1
                break

        if flag==0:
            ni = i + dxy[(d+2)%4][0]
            nj = j + dxy[(d+2)%4][1]

            if 0<=ni<N and 0<=nj<M and visited[ni][nj]!=2:
                queue.append((ni, nj, d))
            else:
                break

move_vacuum()

answer=0
for i in range(N):
    for j in range(M):
        if visited[i][j]==1:
            answer+=1
print(answer)