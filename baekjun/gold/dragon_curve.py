N = int(input())
dragon = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*101 for _ in range(101)]

dxy = [(0,1),(-1,0),(0,-1),(1,0)]
for j,i,d,g in dragon:
    board[i][j]=1

    last_direction = [d]
    for k in range(g):
        for m in range(len(last_direction)-1,-1,-1):
            next_item = (last_direction[m]+1)%4
            last_direction.append(next_item)

    nx, ny = i, j
    for dc in last_direction:
        nx, ny = nx+dxy[dc][0], ny+dxy[dc][1]
        board[nx][ny]=1

answer=0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer+=1
print(answer)