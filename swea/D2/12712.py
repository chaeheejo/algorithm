T = int(input())

dxy = [[(0,1),(0,-1),(1,0),(-1,0)], [(-1,-1),(-1,1),(1,-1),(1,1)]]
def cnt_fly(i,j):
    rtn = 0
    for y in range(2):
        sum = board[i][j]
        for k in range(4):
            nx,ny = i+dxy[y][k][0], j+dxy[y][k][1]
            for _ in range(M-1):
                if 0>nx or nx>=N or 0>ny or ny>=N:
                    break
                sum+=board[nx][ny]
                nx += dxy[y][k][0]
                ny += dxy[y][k][1]
        rtn = max(rtn, sum)
    return rtn

for t in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    answer=0
    for i in range(N):
        for j in range(N):
            answer = max(answer,cnt_fly(i,j))

    print('#%d %d'%(t+1,answer))