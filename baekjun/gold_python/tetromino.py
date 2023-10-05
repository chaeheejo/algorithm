N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(i,j,step,total):
    global answer

    if step==4:
        answer = max(answer, total)
        return

    for k in range(4):
        nx, ny = i+dxy[k][0], j+dxy[k][1]

        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            visited[nx][ny]=1
            dfs(nx,ny,step+1,total+board[nx][ny])
            visited[nx][ny]=0

def use_special(i,j):
    global answer

    for k in range(4):
        total = board[i][j]

        for n in range(3):
            nx, ny = i+dxy[(k+n)%4][0], j+dxy[(k+n)%4][1]

            if 0<=nx<N and 0<=ny<M:
                total += board[nx][ny]

        answer = max(answer, total)

visited = [[0]*M for _ in range(N)]
answer=0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j]=1
            dfs(i,j,1,board[i][j])
            visited[i][j]=0
            use_special(i,j)

print(answer)