T = int(input())

dxy = [(-1,0),(0,-1),(1,0)]

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    print('#%d' %(t+1))
    for k in range(N):
        nx,ny = N-1,k
        for m in range(N):
            print(board[nx-m][ny], end='')
        print(' ', end='')

        nx,ny = N-1-k,N-1
        for m in range(N):
            print(board[nx][ny-m], end='')
        print(' ', end='')

        nx,ny = 0,N-1-k
        for m in range(N):
            print(board[nx+m][ny], end='')
        print()
