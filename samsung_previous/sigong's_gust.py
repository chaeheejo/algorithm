N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

gust_loc=[]
for i in range(N):
    if board[i][0]==-1:
        gust_loc.append([i,0])

clean_way=[]
move = [[(0,1),(-1,0),(0,-1),(1,0)],[(0,1),(1,0),(0,-1),(-1,0)]]
for i in range(2):
    way = []
    x,y = gust_loc[i]
    new = [[0]*M for _ in range(N)]
    for k in range(4):
        while True:
            x+=move[i][k][0]
            y+=move[i][k][1]
            if x<0 or x>=N or y<0 or y>=M or ([x,y] in gust_loc):
                x-=move[i][k][0]
                y-=move[i][k][1]
                break
            way.append([x, y])
            new[x][y] += 1
    clean_way.append(way)

dxy = [(0,1),(-1,0),(0,-1),(1,0)]
def spread_dust():
    global board
    new_board = [b[:] for b in board]
    for i in range(N):
        for j in range(M):
            if board[i][j]==-1:
                continue
            for k in range(4):
                nx,ny = i+dxy[k][0],j+dxy[k][1]
                if 0<=nx<N and 0<=ny<M and board[nx][ny]!=-1:
                    new_board[nx][ny]+=board[i][j]//5
                    new_board[i][j]-=board[i][j]//5
    board = new_board

def clean_dust():
    global board
    new_board = [b[:] for b in board]
    for i in range(2):
        for j in range(len(clean_way[i])):
            cur_x,cur_y = clean_way[i][j]
            if j==0:
                new_board[cur_x][cur_y]=0
            else:
                past_x,past_y = clean_way[i][j-1]
                new_board[cur_x][cur_y] = board[past_x][past_y]
    board = new_board

for _ in range(T):
    spread_dust()
    clean_dust()

answer=0
for i in range(N):
    for j in range(M):
        if board[i][j]!=-1:
            answer+=board[i][j]
print(answer)