N, M = map(int, input().split())
camp = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]

people_store=[]
for _ in range(M):
    x,y = map(int, input().split())
    people_store.append([x-1, y-1])

dxy = [(-1,0),(0,-1),(0,1),(1,0)]
def store_to_camp(si, sj):
    queue=[[si,sj,0]]
    cur=0
    visited=[[0]*N for _ in range(N)]
    visited[si][sj]=1
    candidate=[]
    min_distance=99
    while cur<len(queue):
        x,y,distance = queue[cur]
        cur+=1
        if camp[x][y]==1 and distance<=min_distance:
            min_distance=distance
            candidate.append([distance,x,y])
        for k in range(4):
            nx,ny = x+dxy[k][0],y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if camp[nx][ny]!=-1:
                    queue.append([nx,ny,distance+1])
                visited[nx][ny]=1
    candidate.sort(key=lambda x:(x[0],x[1],x[2]))
    return candidate[0][1],candidate[0][2]

def camp_to_store(pi, pj, si, sj):
    queue=[[pi,pj,-1,[]]]
    cur=0
    visited = [[0]*N for _ in range(N)]
    visited[pi][pj] = 1
    candidate=[]
    min_distance = 99
    while cur<len(queue):
        x,y,priority,path = queue[cur]
        cur+=1
        if x==si and y==sj and len(path)<=min_distance:
            min_distance = len(path)
            candidate.append([priority,path[0][0],path[0][1]])
        for k in range(4):
            nx,ny = x+dxy[k][0],y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if camp[nx][ny]!=-1:
                    if priority==-1:
                        queue.append([nx,ny,k,path[:]+[[nx,ny]]])
                    else:
                        queue.append([nx,ny,priority,path[:]+[[nx,ny]]])
                visited[nx][ny]=1
    candidate.sort(key=lambda x:(x[0]))
    return candidate[0][1],candidate[0][2]

time=0
people = []
while True:
    for i in range(len(people)):
        if people[i][0]==people_store[i][0] and people[i][1]==people_store[i][1]:
            continue
        people[i][0],people[i][1] = camp_to_store(people[i][0],people[i][1],people_store[i][0],people_store[i][1])
        if people[i][0]==people_store[i][0] and people[i][1]==people_store[i][1]:
            camp[people[i][0]][people[i][1]] = -1
    if time<M:
        ci,cj = store_to_camp(people_store[time][0], people_store[time][1])
        camp[ci][cj]=-1
        people.append([ci,cj])
    time += 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if camp[i][j] == -1:
                cnt += 1
    if cnt == M * 2:
        break
print(time)