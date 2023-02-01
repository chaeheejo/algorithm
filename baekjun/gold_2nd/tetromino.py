N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def make_normal_block(depth, result, i, j):
    global answer
    if depth==4:
        answer = max(answer,result)
        return

    for k in range(4):
        nx,ny = i+dxy[k][0], j+dxy[k][1]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
            visited[nx][ny]=1
            make_normal_block(depth + 1, result + board[nx][ny], nx, ny)
            visited[nx][ny]=0

def make_special_block(i,j):
    global answer
    for n in range(4):
        total,flag=board[i][j],0

        for k in range(4):
            if n==k:
                continue
            nx,ny = i+dxy[k][0], j+dxy[k][1]
            if 0<=nx<N and 0<=ny<M:
                total+=board[nx][ny]
            else:
                flag=1
                break
        if flag==0:
            answer = max(answer,total)

answer=0
visited=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j]=1
        make_normal_block(1, board[i][j], i, j)
        make_special_block(i,j)
        visited[i][j]=0
print(answer)