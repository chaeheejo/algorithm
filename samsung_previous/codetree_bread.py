N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
store = []
for _ in range(M):
    i,j = map(int, input().split())
    store.append([i-1,j-1])

def bfs_path(visited,i,j,si,sj):
    queue = [[(i,j)]]
    cur = 0
    visited[i][j] = 1

    while cur < len(queue):
        path = queue[cur]
        cur += 1
        x,y = path[-1][0], path[-1][1]
        if x == si and y == sj:
            return path
        for k in range(4):
            nx, ny = x + dxy[k][0], y + dxy[k][1]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > -1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append(path[:]+[(nx,ny)])
    return -1

def move_people(idx):
    visited=[[0]*N for _ in range(N)]
    path = bfs_path(visited, people[idx][0], people[idx][1], store[idx][0], store[idx][1])
    people[idx][0] = path[1][0]
    people[idx][1] = path[1][1]

def camp(si,sj):
    candidate=[]
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                visited=[[0]*N for _ in range(N)]
                if bfs_path(visited,i,j,si,sj)!=-1:
                    candidate.append([visited[si][sj],i,j])
    candidate.sort(key=lambda x:(x[0],x[1],x[2]))
    return candidate[0][1], candidate[0][2]

people=[]
dxy = [(-1,0),(0,-1),(0,1),(1,0)]
time=0
while True:
    time+=1

    for idx in range(len(people)):
        if people[idx]!=store[idx]:
            move_people(idx)

    flag=0
    for idx in range(len(people)):
        if people[idx]==store[idx]:
            ni, nj = store[idx][0], store[idx][1]
            board[ni][nj] = -1
            continue
        flag=1

    if len(people)==M and flag==0:
        break

    if time-1<M:
        ni,nj = camp(store[time-1][0], store[time-1][1])
        people.append([ni,nj])
        board[ni][nj]=-1

print(time)