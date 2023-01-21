N, M, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ti, tj = map(int, input().split())
ti, tj = ti - 1, tj - 1

passenger_start = []
passenger_destination = []
for _ in range(M):
    si, sj, di, dj = map(int, input().split())
    passenger_start.append([si-1,sj-1])
    passenger_destination.append([di-1,dj-1])

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def find_passenger(si, sj):
    visited = [[0]*N for _ in range(N)]
    queue=[(si, sj)]
    cur=0
    min_distance=1000
    candidate=[]

    while cur<len(queue):
        x, y = queue[cur]
        cur+=1

        if visited[x][y]>min_distance:
            break

        if [x,y] in passenger_start:
            min_distance=visited[x][y]
            candidate.append((x,y))

        else:
            for k in range(4):
                nx,ny = x+dxy[k][0], y+dxy[k][1]
                if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and board[nx][ny]==0:
                    queue.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1

    if candidate:
        candidate.sort()
        x,y = candidate[0][0], candidate[0][1]
        return visited[x][y], x, y
    else:
        return -1, -1, -1

def go_destination(si,sj,di,dj):
    queue = [(si,sj)]
    cur=0
    visited = [[0]*N for _ in range(N)]

    while cur<len(queue):
        x,y = queue[cur]
        cur+=1

        if x==di and y==dj:
            return visited[x][y], x, y

        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y]+1
                queue.append((nx,ny))
    return -1,-1,-1


for _ in range(M):
    gas, pi,pj = find_passenger(ti,tj)
    L -= gas
    if L<0 or gas==-1:
        L=-1
        break

    index = passenger_start.index([pi,pj])
    passenger_start[index] = [-1,-1]

    di,dj = passenger_destination[index]

    gas,pi,pj = go_destination(pi,pj,di,dj)
    L -= gas
    if L<0 or gas==-1:
        L=-1
        break

    L += gas*2
    ti,tj = di,dj

print(L)