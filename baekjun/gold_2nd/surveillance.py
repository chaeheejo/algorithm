N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv=[]
for i in range(N):
    for j in range(M):
        if 0<board[i][j]<6:
            cctv.append([i,j])

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
mode = [[],
        [[0],[1],[2],[3]],
        [[0,1],[2,3]],
        [[0,2],[1,3],[1,2],[0,3]],
        [[0,1,2],[1,2,3],[2,3,0],[0,1,3]],
        [[0,1,2,3]]]
answer=9999
def find_safe_area(depth,tmp_board):
    global answer
    if depth==len(cctv):
        total=0
        for i in range(N):
            total += tmp_board[i].count(0)
        answer = min(answer,total)
        return

    i,j = cctv[depth]
    for m in mode[board[i][j]]:
        original=[]
        for n in m:
            nx,ny = i,j
            while True:
                nx += dxy[n][0]
                ny += dxy[n][1]
                if nx<0 or nx>=N or ny<0 or ny>=M:
                    break
                elif tmp_board[nx][ny]==6:
                    break
                elif tmp_board[nx][ny]==0:
                    tmp_board[nx][ny]=-1
                    original.append([nx,ny])

        find_safe_area(depth+1,[item[:] for item in tmp_board])

        for x,y in original:
            tmp_board[x][y]=0

find_safe_area(0,[item[:] for item in board])
print(answer)