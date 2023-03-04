N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(1,0),(0,-1),(-1,0),(0,1)]
def find_bomb(i,j):
    visited[i][j]=1
    queue=[[i,j]]
    cur,red=0,0
    di,dj=-1,9

    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        if board[x][y]>0:
            if di<x:
                di,dj = x,y
            elif di==x and dj>y:
                di,dj = x,y
        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]==board[i][j]:
                    queue.append([nx,ny])
                    visited[nx][ny]=1
                elif board[nx][ny]==0 and [nx,ny] not in queue:
                    queue.append([nx,ny])
                    red+=1
    return [len(queue),red,di,dj,queue]

def gravity():
    new_board = [[-2]*N for _ in range(N)]
    for j in range(N):
        blank=0
        for i in range(N-1,-1,-1):
            if board[i][j]==-2:
                blank+=1
            elif board[i][j]==-1:
                new_board[i][j]=-1
                blank=0
            else:
                new_board[i+blank][j] = board[i][j]
    return new_board

def rotate():
    new_board = [[0]*N for _ in range(N)]
    for j in range(N):
        tmp=[]
        for i in range(N):
            tmp.append(board[i][j])
        for y in range(N):
            new_board[N-1-j][y] = tmp[y]
    return new_board

answer=0
while True:
    candidate=[]
    max_size=0
    visited=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0 and board[i][j]>0:
                tmp = find_bomb(i,j)
                if tmp[0]>=max_size:
                    max_size = tmp[0]
                    candidate.append(tmp)
    candidate.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))
    if len(candidate)==0:
        break

    size, red = candidate[0][0], candidate[0][1]
    if size<2 or size==red:
        break

    answer+=size*size
    for i,j in candidate[0][4]:
        board[i][j]=-2

    board = gravity()
    board = rotate()
    board = gravity()

print(answer)