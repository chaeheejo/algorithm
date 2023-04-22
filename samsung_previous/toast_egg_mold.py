N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def share_egg(i,j):
    queue=[[i,j]]
    cur=0
    visited=[[0]*N for _ in range(N)]
    visited[i][j]=1
    total=board[i][j]
    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        for k in range(4):
            nx,ny = x+dxy[k][0],y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                diff = abs(board[x][y]-board[nx][ny])
                if diff>=L and diff<=R:
                    queue.append([nx,ny])
                    total+=board[nx][ny]
                    visited[nx][ny]=1
    for x,y in queue:
        new_board[x][y] = total//len(queue)

answer=0
while True:
    new_board = [b[:] for b in board]
    for i in range(N):
        for j in range(N):
            if board[i][j]==new_board[i][j]:
                share_egg(i,j)
    flag=0
    for i in range(N):
        for j in range(N):
            if board[i][j]!=new_board[i][j]:
                flag=1
    if flag==0:
        break
    board = new_board
    answer+=1
print(answer)