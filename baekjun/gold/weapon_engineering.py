N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxy=[(0,-1,1,0),(-1,0,0,-1),(-1,0,0,1),(0,1,1,0)]
answer=0
def make_weapon(i,j,num):
    global answer
    if j==M :
        i+=1
        j=0

    if i==N:
        answer = max(answer, num)
        return

    if not visited[i][j]:
        for k in range(4):
            a,b,c,d = dxy[k]
            nx,ny,kx,ky = i+a, j+b, i+c, j+d
            if 0<=nx<N and 0<=ny<M and 0<=kx<N and 0<=ky<M :
                if visited[nx][ny]==0 and visited[kx][ky]==0:
                    visited[nx][ny],visited[kx][ky],visited[i][j] = 1,1,1
                    make_weapon(i,j+1, num + board[i][j]*2 + board[nx][ny] + board[kx][ky])
                    visited[nx][ny],visited[kx][ky],visited[i][j] = 0,0,0
    make_weapon(i,j+1,num)

visited=[[0]*M for _ in range(N)]
make_weapon(0,0,0)
print(answer)