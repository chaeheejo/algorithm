N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

board = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if maze[i][j]==0:
            board[i][j]=-1
        elif maze[i][j]==1:
            board[i][j]=0

board[0][0]=1
queue=[(0,0)]
cur=0
dxy=[(1,0),(-1,0),(0,1),(0,-1)]
while cur<len(queue):
    i, j = queue[cur]
    cur+=1

    for k in range(4):
        nx = i+dxy[k][0]
        ny = j+dxy[k][1]

        if 0<=nx<N and 0<=ny<M and board[nx][ny]==0:
            board[nx][ny]=board[i][j]+1
            queue.append((nx,ny))

print(board[N-1][M-1])