N, M, K = map(int, input().split())

board = [[-1]*M for _ in range(N)]
virus_xy,virus_detail=[],[]
for k in range(K):
    x,y,s,d,b = map(int, input().split())
    if d==3:
        d=2
    elif d==2:
        d=3
    virus_xy.append([x-1,y-1])
    virus_detail.append([s,d-1,b])
    board[x-1][y-1] = k

def catch_virus(j):
    for i in range(N):
        if board[i][j]!=-1:
            cur = board[i][j]
            b = virus_detail[cur][-1]
            virus_xy[cur][0]=-1
            board[i][j]=-1
            return b
    return 0

def update_move(new_board,nx,ny,k):
    b = virus_detail[k][-1]
    if new_board[nx][ny] != -1:
        cur = new_board[nx][ny]
        if virus_detail[cur][-1] < b:
            virus_xy[cur][0] = -1
            virus_xy[k] = [nx, ny]
            new_board[nx][ny] = k
        else:
            virus_xy[k][0] = -1
    else:
        new_board[nx][ny] = k
        virus_xy[k] = [nx, ny]

dxy = [(-1,0),(0,1),(1,0),(0,-1)]
def move_virus():
    global board
    new_board = [[-1]*M for _ in range(N)]
    for k in range(K):
        x,y = virus_xy[k]
        if x==-1:
            continue
        s,d,b = virus_detail[k]
        nx,ny = x,y
        for _ in range(s):
            nx,ny = nx+dxy[d][0],ny+dxy[d][1]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                d = (d+2)%4
                nx,ny = nx+dxy[d][0]*2,ny+dxy[d][1]*2
        virus_detail[k][1] = d
        update_move(new_board,nx, ny, k)
    board = new_board

answer=0
for j in range(M):
    answer+=catch_virus(j)
    move_virus()
print(answer)