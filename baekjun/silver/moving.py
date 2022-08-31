N, M = map(int, input().split())

maze=[]
for _ in range(N):
    tmp = list(map(int, input().split()))
    maze.append(tmp)

answer = [[0]*M for _ in range(N)]
def count_candy():
    for i in range(N):
        for j in range(M):
            if i==0 and j==0:
                answer[i][j]=maze[i][j]
            elif i==0:
                answer[i][j] = answer[i][j-1]+maze[i][j]
            elif j==0:
                answer[i][j] = answer[i-1][j]+maze[i][j]
            else:
                answer[i][j] = max(answer[i][j-1], answer[i-1][j]) + maze[i][j]

count_candy()
print(answer[N-1][M-1])