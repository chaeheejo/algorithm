N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
board = [[0]*M for _ in range(N)]

water=[]
start_i, start_j, end_i, end_j =0,0,0,0
for i in range(N):
    for j in range(M):
        if maze[i][j]=='S':
            start_i, start_j = i,j
            board[i][j]=1
        elif maze[i][j]=='D':
            end_i, end_j = i,j
            board[i][j]=-100
        elif maze[i][j]=='.':
            board[i][j]=0
        elif maze[i][j]=='*':
            water.append((i,j,0))
            board[i][j]=-1
        else:
            board[i][j]=-1


dxy=[(1,0),(-1,0),(0,1),(0,-1)]
escape=[(start_i,start_j,0)]
index_water, index_escape = 0,0
level_water, level_escape = 0,0
flag=0
while True:
    while index_water<len(water):
        water_i, water_j, cur_water = water[index_water]
        index_water += 1

        if level_water!=cur_water:
            index_water -= 1
            break

        for k in range(4):
            nx, ny = water_i+dxy[k][0], water_j+dxy[k][1]

            if 0<=nx<N and 0<=ny<M and board[nx][ny] >= 0:
                board[nx][ny]=-1
                water.append((nx,ny,cur_water+1))
    level_water+=1

    while index_escape<len(escape):
        escape_i, escape_j, cur_escape = escape[index_escape]
        index_escape += 1

        if escape_i == end_i and escape_j == end_j:
            flag=1
            break
        if level_escape!=cur_escape:
            index_escape-=1
            break

        for k in range(4):
            nx, ny = escape_i + dxy[k][0], escape_j + dxy[k][1]

            if 0<=nx<N and 0<=ny<M :
                if board[nx][ny]==0 or board[nx][ny]==-100:
                    board[nx][ny] = cur_escape+1
                    escape.append((nx, ny, cur_escape+1))
    level_escape+=1

    if flag==1:
        break
    if index_water==len(water) and index_escape==len(escape):
        break

if flag:
    print(board[end_i][end_j])
else:
    print('KAKTUS')