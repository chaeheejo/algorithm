N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if 0<office[i][j]<6:
            cctv.append([i, j])

def mark_watch(temp_office, mode, x, y):
    for m in mode:
        nx, ny = x, y
        while True:
            nx += dx[m]
            ny += dy[m]

            if nx <0 or nx >=N or ny <0 or ny >=M:
                break
            elif temp_office[nx][ny]==6:
                break
            elif temp_office[nx][ny]==0:
                temp_office[nx][ny]=-1

answer=9999
def watch_cctv(array, r):
    global answer

    if r==len(cctv):
        cnt=0
        for i in range(N):
            cnt += array[i].count(0)
        answer = min(answer, cnt)
        return

    temp_office = [item[:] for item in array]
    i, j = cctv[r]
    for m in mode[office[i][j]]:
        mark_watch(temp_office, m, i, j)
        watch_cctv(temp_office, r+1)
        temp_office = [item[:] for item in array]

watch_cctv(office, 0)
print(answer)