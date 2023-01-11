N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]

way= [0]*26
way[ord(board[0][0])-65]=1
answer=0
def dfs(i, j, num):
    global answer

    answer = max(answer, num)

    for k in range(4):
        nx, ny = i+dxy[k][0], j+dxy[k][1]

        if 0<=nx<N and 0<=ny<M and way[ord(board[nx][ny])-65]==0:
            way[ord(board[nx][ny])-65] = 1
            temp=num+1
            dfs(nx, ny, temp)
            way[ord(board[nx][ny])-65] = 0

dfs(0,0,1)
print(answer)