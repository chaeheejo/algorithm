N, M = map(int, input().split())

maze=[]
for _ in range(N):
    tmp = list(map(int, input().split()))
    maze.append(tmp)

answer = []
def count_candy(r, c, candy):
    candy += maze[r][c]

    if r==N-1 and c==M-1:
        return answer.append(candy)

    if r+1<N and c<M:
        count_candy(r + 1, c, candy)
    if r<N and c+1<M:
        count_candy(r, c + 1, candy)
    if r+1<N and c+1<M:
        count_candy(r + 1, c + 1, candy)
    return

count_candy(0, 0, 0)
print(max(answer))