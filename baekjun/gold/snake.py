N = int(input())
K = int(input())

board = [[0]*N for _ in range(N)]
for _ in range(K):
    i,j = map(int, input().split())
    board[i-1][j-1] = 200

L = int(input())
rotate = [list(input().split()) for _ in range(L)]

r_idx=0
board[0][0],d = 1,3
snake=[(0,0)]
dxy = [(-1,0),(0,-1),(1,0),(0,1)]
answer=0
for k in range(1,10001):
    nx,ny = snake[0][0]+dxy[d][0], snake[0][1]+dxy[d][1]
    if nx<0 or nx>=N or ny<0 or ny>=N:
        answer=k
        break
    if board[nx][ny]==1:
        answer=k
        break

    snake.insert(0,(nx,ny))

    if board[nx][ny]==0:
        i,j = snake.pop()
        board[i][j]=0

    board[nx][ny]=1

    if r_idx<L and k==int(rotate[r_idx][0]):
        if rotate[r_idx][1]=='L':
            d = (d+1)%4
        else:
            d = (d-1)%4
        r_idx+=1

print(answer)