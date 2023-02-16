N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

teams = []
dxy = [(0,1),(-1,0),(0,-1),(1,0)]
def find_team(i, j):
    queue=[[[i,j]]]
    cur=0
    visited = [[0]*N for _ in range(N)]
    candidate=[]

    while cur<len(queue):
        way = queue[cur]
        x,y = way[-1]
        visited[x][y]=1
        cur+=1

        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]==3:
                    candidate.append(way[:] + [[nx, ny]])
                    continue
                elif board[nx][ny]==2:
                    queue.append(way[:]+[[nx,ny]])
                visited[nx][ny]=1
    return candidate[-1]

for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            teams.append(find_team(i, j))

def change_head_tail(m):
    tmp = teams[m][:]
    cur=len(teams[m])-1
    for i in range(len(teams[m])):
        teams[m][i] = tmp[cur]
        cur-=1

    for i in range(len(teams[m])):
        x, y = teams[m][i]
        if i == 0:
            board[x][y] = 1
        elif i == len(teams[m]) - 1:
            board[x][y] = 3
        else:
            board[x][y] = 2


def get_score(i, j):
    global answer

    for t in range(M):
        if [i,j] in teams[t]:
            dist = teams[t].index([i,j])
            answer += (dist+1)**2
            change_head_tail(t)
            return

answer=0
rxy = [(1,0),(0,1),(-1,0),(0,-1)]
ri,rj,rd,d = -1,0,0,0
for r in range(K):
    for m in range(M):
        hi,hj = teams[m][0]

        for k in range(4):
            nx,ny = hi+dxy[k][0], hj+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and (board[nx][ny]==4 or board[nx][ny]==3):
                new_team = [[nx,ny]]+teams[m][:-1]

                for i in range(len(teams[m])):
                    x,y = teams[m][i]
                    board[x][y] = 4

                for i in range(len(teams[m])):
                    teams[m][i] = new_team[i]

                for i in range(len(teams[m])):
                    x,y = teams[m][i]
                    if i==0:
                        board[x][y] = 1
                    elif i==len(teams[m])-1:
                        board[x][y] = 3
                    else:
                        board[x][y] = 2
                break

    new_ri,new_rj = ri+rxy[rd][0], rj+rxy[rd][1]
    if 0<=new_ri<N and 0<=new_rj<N:
        ri,rj = new_ri,new_rj
    else:
        rd = (rd+1)%4
        ri,rj = ri+rxy[rd][0], rj+rxy[rd][1]

    if d!=(r//N)%4:
        ri,rj = ri-rxy[rd][0], rj-rxy[rd][1]
        d = (r//N)%4

    ball_i, ball_j = ri,rj
    while 0<=ball_i<N and 0<=ball_j<N:
        if 1<=board[ball_i][ball_j]<=3:
            get_score(ball_i, ball_j)
            break
        ball_i+=dxy[d][0]
        ball_j+=dxy[d][1]

print(answer)