N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
cmd = list(map(int, input().split()))

def rotate(l):
    for i in range(0, 2**N, 2**l):
        for j in range(0, 2**N, 2**l):
            new_board = [board[k][j:j+2**l] for k in range(i, i+2**l)]
            new_board = list(zip(*new_board[::-1]))
            for x in range(2**l):
                for y in range(2**l):
                    board[x+i][y+j] = new_board[x][y]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def firestorm(board):
    new_board = [item[:] for item in board[:]]
    for i in range(2**N):
        for j in range(2**N):
            near=0

            for k in range(4):
                nx, ny = i+dxy[k][0], j+dxy[k][1]

                if 0<=nx<2**N and 0<=ny<2**N and board[nx][ny]>0:
                    near+=1

            if near>=3:
                continue
            new_board[i][j]-=1

    return new_board

def count_block(i,j):
    queue=[(i,j)]
    cur=0
    visited[i][j]=1

    while cur<len(queue):
        x,y = queue[cur]
        cur+=1

        for k in range(4):
            nx, ny = x + dxy[k][0], y + dxy[k][1]

            if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and visited[nx][ny]==0:
                if board[nx][ny]>0:
                    queue.append((nx,ny))
                    visited[nx][ny]=1

    return len(queue)

for c in cmd:
    if c>0:
        rotate(c)
    board = firestorm(board)

total=0
for i in range(2**N):
    for j in range(2**N):
        if board[i][j]>0:
            total+=board[i][j]
print(total)

visited=[[0]*(2**N) for _ in range(2**N)]
answer=0
for i in range(2**N):
    for j in range(2**N):
        if visited[i][j]==0 and board[i][j]>0:
            answer = max(answer,count_block(i,j))

if answer==1:
    answer=0
print(answer)