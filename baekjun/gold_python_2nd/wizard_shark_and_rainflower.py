N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for d,s in move:
    cloud_move=[]
    dxy = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

    for x,y in cloud:
        nx,ny = (x+dxy[d-1][0]*s)%N,(y+dxy[d-1][1]*s)%N
        cloud_move.append((nx, ny))
        board[nx][ny]+=1

    dxy = [(-1,-1),(-1,1),(1,1),(1,-1)]
    for x,y in cloud_move:
        neighbor=0
        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]>0:
                neighbor+=1
        board[x][y]+=neighbor

    new_cloud=[]
    for i in range(N):
        for j in range(N):
            if board[i][j]>=2 and (i,j) not in cloud_move:
                new_cloud.append((i,j))
                board[i][j]-=2
    cloud = new_cloud

answer=0
for i in range(N):
    for j in range(N):
        answer+=board[i][j]
print(answer)