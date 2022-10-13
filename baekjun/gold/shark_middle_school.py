N, M = map(int, input().split())
map_block = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make_block_group(m, n, color):
    cur=0
    queue=[[m,n]]
    candidate_group, rainbows = [[m,n]], []

    while cur<len(queue):
        i, j = queue[cur]
        cur+=1

        for k in range(4):
            tmp_i, tmp_j = i+dx[k], j+dy[k]
            if 0<=tmp_i<N and 0<=tmp_j<N and not visited[tmp_i][tmp_j]:
                if map_block[tmp_i][tmp_j]==color:
                    visited[tmp_i][tmp_j]=True
                    queue.append([tmp_i,tmp_j])
                    candidate_group.append([tmp_i,tmp_j])
                elif map_block[tmp_i][tmp_j]==0:
                    visited[tmp_i][tmp_j] = True
                    queue.append([tmp_i,tmp_j])
                    rainbows.append([tmp_i,tmp_j])
                    candidate_group.append([tmp_i, tmp_j])

    for i, j in rainbows:
        visited[i][j]=False

    return [len(candidate_group), len(rainbows), candidate_group]

def remove_block(blocks):
    for i, j in blocks:
        map_block[i][j]=-99

def gravity(map_block):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if map_block[i][j]<=-1:
                continue
            cur=i
            while True:
                if 0<=cur+1<N and map_block[cur + 1][j]==-99:
                    cur+=1
                else:
                    break
            if cur!=i:
                map_block[cur][j] = map_block[i][j]
                map_block[i][j]=-99


def rotate():
    new = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[N-1-j][i] = map_block[i][j]
    return new

answer=0
while True:
    visited=[[False]*N for _ in range(N)]
    block_group=[]
    for i in range(N):
        for j in range(N):
            if map_block[i][j]>0 and not visited[i][j]:
                visited[i][j] = True
                blocks = make_block_group(i, j, map_block[i][j])

                if blocks[0]>=2:
                    block_group.append(blocks)

    if not block_group:
        break

    block_group.sort(reverse=True)

    remove_block(block_group[0][2])
    answer+=block_group[0][0]**2

    gravity(map_block)
    map_block=rotate()
    gravity(map_block)

print(answer)