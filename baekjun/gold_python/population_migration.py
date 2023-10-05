N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(1,0),(-1,0),(0,1),(0,-1)]
def move(i,j):
    queue=[(i,j)]
    cur=0

    while cur<len(queue):
        x,y = queue[cur]
        cur+=1

        for k in range(4):
            nx, ny = x+dxy[k][0], y+dxy[k][1]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if L<=abs(board[x][y]-board[nx][ny])<=R:
                    visited[nx][ny]=1
                    visited[x][y]=1
                    queue.append((nx,ny))
    if len(queue)>1:
        update(queue)

def update(queue):
    num, total = len(queue), 0
    for i in range(N):
        for j in range(N):
            if (i,j) in queue:
                total += board[i][j]

    for i,j in queue:
        board[i][j] = int(total/num)

answer=0
while True:
    visited=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                move(i,j)

    num = 0
    for v in visited:
        num += v.count(1)

    if num==0:
        break

    answer+=1

print(answer)