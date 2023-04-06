N, M, K = map(int, input().split())
extra_feed = [list(map(int, input().split())) for _ in range(N)]
feed = [[5]*N for _ in range(N)]

board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r,c,a = map(int, input().split())
    board[r-1][c-1].append(a)

def eat_feed():
    global board
    new_feed = [[0]*N for _ in range(N)]
    new_board = [[r[:] for r in b] for b in board]
    for i in range(N):
        for j in range(N):
            if len(board[i][j])==0:
                continue
            for k in range(len(board[i][j])):
                if feed[i][j]-board[i][j][k]>=0:
                    feed[i][j]-=board[i][j][k]
                    new_board[i][j][k]+=1
                else:
                    for r in range(k,len(board[i][j])):
                        new_feed[i][j]+=board[i][j][r]//2
                        new_board[i][j].pop()
                    break
    for i in range(N):
        for j in range(N):
            feed[i][j]+=new_feed[i][j]
    board = new_board

dxy = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def make_virus():
    global board
    new_board = [[r[:] for r in b] for b in board]
    for i in range(N):
        for j in range(N):
            if len(board[i][j])==0:
                continue
            for k in range(len(board[i][j])):
                if board[i][j][k]%5==0:
                    for d in range(8):
                        nx,ny = i+dxy[d][0],j+dxy[d][1]
                        if 0<=nx<N and 0<=ny<N:
                            new_board[nx][ny].insert(0,1)
    board = new_board

for _ in range(K):
    eat_feed()
    make_virus()
    for i in range(N):
        for j in range(N):
            feed[i][j]+=extra_feed[i][j]

answer=0
for i in range(N):
    for j in range(N):
        answer+=len(board[i][j])
print(answer)