N = int(input())
student_like = [list(map(int, input().split())) for _ in range(N*N)]
seat = [[0]*N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for n in range(N*N):
    student = student_like[n]
    tmp=[]

    for i in range(N):
        for j in range(N):
            if seat[i][j]==0:
                like=0
                blank=0
                for k in range(4):
                    tx, ty = i+dx[k], j+dy[k]
                    if 0<=tx<N and 0<=ty<N:
                        if seat[tx][ty] in student[1:]:
                            like+=1
                        if seat[tx][ty]==0:
                            blank+=1
                tmp.append([like, blank, i, j])
    tmp.sort(key= lambda f:(-f[0], -f[1], f[2], f[3]))
    seat[tmp[0][2]][tmp[0][3]] = student[0]

answer=0
student_like.sort()

for i in range(N):
    for j in range(N):
        total=0
        for k in range(4):
            tx, ty = i+dx[k], j+dy[k]
            if 0<=tx<N and 0<=ty<N:
                if seat[tx][ty] in student_like[seat[i][j]-1]:
                    total+=1
        if total!=0:
            answer+=10**(total-1)

print(answer)