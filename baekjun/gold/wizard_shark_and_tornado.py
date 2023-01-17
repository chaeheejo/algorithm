N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

sand0 = [[0,0,2,0,0],[0,10,7,1,0],[5,100,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
sand1 = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,100,10,0],[0,0,5,0,0]]
sand2 = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,100,5],[0,1,7,10,0],[0,0,2,0,0]]
sand3 = [[0,0,5,0,0],[0,10,100,10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]
sand = [sand0,sand1,sand2,sand3]

def move_tornado(i,j,cur_direction):
    global answer

    update_sand = sand[cur_direction]
    nx, ny = 0,0
    total = board[i][j]
    for n in range(i - 2, i + 3):
        ny = 0

        for m in range(j - 2, j + 3):
            if update_sand[nx][ny] == 100:
                ny += 1
                continue

            new = int(0.01 * update_sand[nx][ny] * board[i][j])
            if 0 <= n < N and 0 <= m < N:
                board[n][m] += new
            else:
                answer += new
            total -= new

            ny += 1
        nx += 1

    ai,aj = i+tornado_dxy[cur_direction][0], j+tornado_dxy[cur_direction][1]
    if 0 <= ai < N and 0 <= aj < N:
        board[ai][aj] += total
    else:
        answer += total
    board[i][j]=0

tornado_dxy = [(0,-1),(1,0),(0,1),(-1,0)]

answer, cur_direction=0,0
flag, cnt = 1,0
i,j = N//2, N//2
while True:
    if i==0 and j==-1:
        break

    cnt+=1
    if cnt==3:
        flag+=1
        cnt=1

    for k in range(flag):
        i,j = i+tornado_dxy[cur_direction][0], j+tornado_dxy[cur_direction][1]
        if board[i][j]>0:
            move_tornado(i,j,cur_direction)

    cur_direction = (cur_direction+1) %4

print(answer)