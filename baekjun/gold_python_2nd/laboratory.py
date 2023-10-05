N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

candidate=[]
for i in range(N):
    for j in range(M):
        if board[i][j]==0:
            candidate.append((i, j))

dxy = [(0,1),(1,0),(-1,0),(0,-1)]
def spread_virus(board,i,j):
    queue=[(i,j)]
    cur=0

    while cur<len(queue):
        x,y = queue[cur]
        cur+=1

        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and board[nx][ny]==0:
                board[nx][ny]=2
                visited[nx][ny]=1
                queue.append((nx,ny))

def cnt_safe_area(board):
    cnt=0
    for i in range(N):
        for j in range(M):
            if board[i][j]==0:
                cnt+=1
    return cnt

def combination(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:],r-1):
                yield [array[i]]+next

answer=0
for comb in combination(range(len(candidate)), 3):
    new_board = [b[:] for b in board]

    for c in comb:
        x,y = candidate[c][0], candidate[c][1]
        new_board[x][y]=1

    visited=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if new_board[i][j]==2 and visited[i][j]==0:
                spread_virus(new_board,i,j)

    answer = max(answer, cnt_safe_area(new_board))
print(answer)