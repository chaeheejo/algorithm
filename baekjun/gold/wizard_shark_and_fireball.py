N, M, K = map(int, input().split())
fireball = []
for _ in range(M):
    i,j,m,s,d = list(map(int, input().split()))
    fireball.append([i-1,j-1,m,s,d])

board = [[[] for _ in range(N)] for _ in range(N)]

dxy = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
for _ in range(K):

    while fireball:
        x,y,m,s,d = fireball.pop(0)
        nx, ny = (x+dxy[d][0]*s)%N, (y+dxy[d][1]*s)%N
        board[nx][ny].append([m,s,d])

    for i in range(N):
        for j in range(N):
            if len(board[i][j])>=2:
                mass, speed, length = 0,0,len(board[i][j])
                cnt_odd, cnt_even = 0,0

                while board[i][j]:
                    m,s,d = board[i][j].pop(0)
                    mass += m
                    speed += s

                    if d%2==0:
                        cnt_even +=1
                    else:
                        cnt_odd += 1

                if mass//5>0:
                    direction = []
                    if cnt_odd==length or cnt_even==length:
                        direction = [0,2,4,6]
                    else:
                        direction = [1,3,5,7]

                    for k in range(4):
                        fireball.append([i,j,mass//5, speed//length,direction[k]])

            if len(board[i][j])==1:
                fireball.append([i,j]+board[i][j].pop(0))

answer=sum([fire[2] for fire in fireball])
print(answer)