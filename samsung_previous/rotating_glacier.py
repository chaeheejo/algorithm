N, Q = map(int, input().split())
N = 2**N
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))

dxy = [(0,1),(1,0),(-1,0),(0,-1)]
def move(new_board, r, start_row, start_col, d):
    for i in range(start_row, start_row+r):
        for j in range(start_col, start_col+r):
            nx = i + dxy[d][0] * r
            ny = j + dxy[d][1] * r
            new_board[nx][ny] = board[i][j]

def rotate(l):
    r = 2**(l-1)
    new_board = [b[:] for b in board]
    for x in range(0,N,2**l):
        for y in range(0,N,2**l):
            move(new_board,r,x,y,0)
            move(new_board,r,x,y+r,1)
            move(new_board,r,x+r,y,2)
            move(new_board,r,x+r,y+r,3)
    return new_board

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
        board = rotate(k)
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