N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

up, down = 0, 0
for i in range(N):
    if board[i][0]==-1 :
        up=i
        down=i+1
        break

for _ in range(T):
    spread_board = [[0] * M for _ in range(N)]
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(N):
        for j in range(M):
            if board[i][j]>0:
                cnt=0
                update=[]

                for k in range(4):
                    nx, ny = i+dxy[k][0], j+dxy[k][1]

                    if 0<=nx<N and 0<=ny<M and board[nx][ny]!=-1:
                        cnt+=1
                        update.append((nx,ny))

                new = board[i][j]//5
                for nx, ny in update:
                    spread_board[nx][ny] += new
                spread_board[i][j] += (board[i][j] - new * cnt)
            else:
                spread_board[i][j] += board[i][j]
    board = spread_board

    dxy = [(0,1),(-1,0),(0,-1),(1,0)]
    x, y, d, tmp = up, 1, 0, 0
    while True:
        nx,ny = x+dxy[d][0], y+dxy[d][1]
        if x==up and y==0:
            break
        elif nx<0 or nx>=N or ny<0 or ny>=M:
            d += 1
            continue
        board[x][y], tmp = tmp, board[x][y]
        x, y = nx,ny

    dxy = [(0,1), (1,0), (0,-1), (-1,0)]
    x, y, d, tmp = down, 1, 0, 0
    while True:
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if x == down and y == 0:
            break
        elif nx < 0 or nx >= N or ny < 0 or ny >= M:
            d += 1
            continue
        board[x][y], tmp = tmp, board[x][y]
        x, y = nx, ny

answer=0
for i in range(N):
    for j in range(M):
        if board[i][j]>0:
            answer+=board[i][j]
print(answer)