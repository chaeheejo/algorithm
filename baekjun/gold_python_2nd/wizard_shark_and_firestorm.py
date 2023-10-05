N, Q = map(int, input().split())
N = 2**N
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

def rotate(l):
    new_board = [b[:] for b in board]
    for k in range(0,N,l):
        for i in range(k,N,l):
            for j in range(k,N,l):
                for n in range(l):
                    tmp = []
                    for m in range(l):
                        tmp.append(board[i+n][j+m])
                    for x in range(l):
                        new_board[i+x][j+l-1-n]=tmp[x]
    return new_board

dxy = [(1,0),(-1,0),(0,1),(0,-1)]
def melt():
    new_board = [b[:] for b in board]
    for i in range(N):
        for j in range(N):
            if board[i][j]>0:
                neighbor=0
                for k in range(4):
                    nx,ny = i+dxy[k][0],j+dxy[k][1]
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]>0:
                        neighbor+=1
                if neighbor<3:
                    new_board[i][j]-=1
    return new_board

for k in cmd:
    if k!=0:
        board = rotate(2**k)
    board = melt()

total = 0
for i in range(N):
    for j in range(N):
        total+=board[i][j]
print(total)

def find_group(i,j):
    queue=[[i,j]]
    cur=0
    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        for k in range(4):
            nx,ny = x+dxy[k][0],y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and board[nx][ny]>0:
                queue.append([nx,ny])
                visited[nx][ny]=1
    return len(queue)

max_group=0
visited=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0 and board[i][j]>0:
            visited[i][j]=1
            max_group = max(max_group,find_group(i,j))
print(max_group)