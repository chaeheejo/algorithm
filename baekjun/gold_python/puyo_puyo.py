board = [list(input()) for _ in range(12)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def pop(n,m):
    queue=[(n,m)]
    cur=0
    queue_pop=[(n,m)]
    visited = [[0] * 6 for _ in range(12)]
    visited[n][m]=1
    while cur<len(queue):
        i,j = queue[cur]
        cur+=1

        for k in range(4):
            nx, ny = i+dxy[k][0], j+dxy[k][1]

            if 0<=nx<12 and 0<=ny<6 and visited[nx][ny]==0:
                if board[nx][ny]==board[i][j]:
                    queue_pop.append((nx,ny))
                    queue.append((nx,ny))
                    visited[nx][ny] = 1

    if len(queue_pop)>=4:
        for i,j in queue_pop:
            board[i][j]='.'
        return 1
    else:
        return 0

def gravity():
    for j in range(6):
        queue=[]
        cur=0
        for i in range(11,-1,-1):
            if board[i][j]!='.':
                queue.append(board[i][j])
        for i in range(11,-1,-1):
            if cur<len(queue):
                x = queue[cur]
                cur+=1
                board[i][j]=x
            else:
                board[i][j]='.'

answer=0
while True:
    result=0
    for i in range(12):
        for j in range(6):
            if board[i][j]!='.':
                result+=pop(i,j)

    if result>0:
        answer+=1
    else:
        break

    gravity()
print(answer)