N = int(input())
student = [list(map(int, input().split())) for _ in range(N**2)]
board =[[0]*N for _ in range(N)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
for s in student:
    blank=[]
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                zero,like=0,0
                for k in range(4):
                    nx,ny = i+dxy[k][0], j+dxy[k][1]
                    if 0<=nx<N and 0<=ny<N:
                        if board[nx][ny]==0:
                            zero+=1
                        elif board[nx][ny] in s[1:]:
                            like+=1
                blank.append([like,zero,i,j])
    blank.sort(key= lambda x:(-x[0],-x[1],x[2],x[3]))

    x,y = blank[0][2],blank[0][3]
    board[x][y] = s[0]

student.sort()
answer=0
for i in range(N):
    for j in range(N):
        like=0
        for k in range(4):
            nx,ny = i+dxy[k][0], j+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] in student[board[i][j]-1][1:]:
                like+=1
        if like>=1:
            answer+=10**(like-1)

print(answer)