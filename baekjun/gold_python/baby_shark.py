N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def eat_fish(i,j):
    queue = [(i,j,0)]
    cur=0
    visited[i][j]=1
    candidate=[]

    while cur<len(queue):
        x,y,n = queue[cur]
        cur+=1

        for k in range(4):
            nx, ny = x+dxy[k][0], y+dxy[k][1]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]==board[i][j] or board[nx][ny]==0:
                    visited[nx][ny]=1
                    queue.append((nx,ny,n+1))
                elif board[nx][ny]<board[i][j]:
                    candidate.append((nx,ny,n+1))

    if len(candidate)>0:
        candidate.sort(key=lambda x : (x[2],x[0],x[1]))
        return candidate[0]
    else:
        return -1,-1,-1

shark_x, shark_y = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j]==9:
            shark_x=i
            shark_y = j
            break
    if shark_x!=0:
        break
board[shark_x][shark_y]=2

answer,weight,flag=0,2,2
while True:
    visited = [[0]*N for _ in range(N)]
    rtn_x, rtn_y, time = eat_fish(shark_x,shark_y)

    if rtn_x==-1:
        break

    answer += time

    flag-=1
    if flag==0:
        weight +=1
        flag = weight

    board[rtn_x][rtn_y] = weight
    board[shark_x][shark_y] = 0
    shark_x, shark_y = rtn_x, rtn_y

print(answer)