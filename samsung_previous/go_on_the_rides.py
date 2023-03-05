N = int(input())
students = [list(map(int, input().split())) for _ in range(N * N)]
board = [[0]*N for _ in range(N)]

def count(i,j,favorite):
    cnt_favorite, cnt_blank = 0,0
    for k in range(4):
        nx,ny = i+dxy[k][0], j+dxy[k][1]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny] in favorite:
                cnt_favorite += 1
            elif board[nx][ny] == 0:
                cnt_blank += 1
    return cnt_favorite,cnt_blank

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
for n in range(N*N):
    student = students[n][0]
    favorite = students[n][1:]
    candidate=[]
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                cnt_favorite, cnt_blank = count(i,j,favorite)
                candidate.append([cnt_favorite, cnt_blank, i, j])
    candidate.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    nx, ny = candidate[0][-2], candidate[0][-1]
    board[nx][ny] = student

students.sort()
answer=0
for i in range(N):
    for j in range(N):
        student = board[i][j]
        cnt_favorite, _ = count(i,j,students[student-1][1:])
        if cnt_favorite==0:
            continue
        answer+=10**(cnt_favorite - 1)
print(answer)