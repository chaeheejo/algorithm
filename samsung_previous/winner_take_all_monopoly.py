N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

player_d=list(map(int, input().split()))
for m in range(M):
    player_d[m]-=1

priority=[]
for _ in range(M):
    one_priority=[]
    for _ in range(4):
        d1,d2,d3,d4 = map(int, input().split())
        one_priority.append([d1-1,d2-1,d3-1,d4-1])
    priority.append(one_priority)

contract=[[[0,0] for _ in range(N)] for _ in range(N)]
def update_contract():
    for i in range(N):
        for j in range(N):
            if board[i][j]>0:
                contract[i][j]=[board[i][j],K]
            else:
                if contract[i][j][1]>0:
                    contract[i][j][1]-=1

def move_player(i,j):
    p = board[i][j]-1
    d = player_d[p]
    for k in range(4):
        cur_p = priority[p][d][k]
        x,y = i+dxy[cur_p][0],j+dxy[cur_p][1]
        if 0<=x<N and 0<=y<N and contract[x][y][1]==0:
            new_board[x][y].append(board[i][j])
            player_d[p] = cur_p
            return
    for k in range(4):
        cur_p = priority[p][d][k]
        x,y = i+dxy[cur_p][0],j+dxy[cur_p][1]
        if 0<=x<N and 0<=y<N and contract[x][y][0]==board[i][j]:
            new_board[x][y].append(board[i][j])
            player_d[p] = cur_p
            return

dxy = [(-1,0),(1,0),(0,-1),(0,1)]
answer=-1

update_contract()

for m in range(1000):
    new_board=[[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]>0:
                move_player(i,j)

    board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(new_board[i][j])>0:
                min_p = min(new_board[i][j])
                board[i][j] = min_p

    update_contract()

    end=1
    for i in range(N):
        for j in range(N):
            if board[i][j]>1:
                end=0
    if end==1:
        answer=m+1
        break

print(answer)