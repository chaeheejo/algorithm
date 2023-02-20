M, T = map(int, input().split())

pic_i,pic_j = map(int, input().split())
pic_i, pic_j = pic_i-1,pic_j-1

board = [[[0]*8 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    i,j,d = map(int, input().split())
    board[i-1][j-1][d-1] +=1

pxy = [(-1,0),(0,-1),(1,0),(0,1)]
def find_path():
    queue=[[pic_i,pic_j,0,[]]]
    cur=0
    candidate=[]
    while cur<len(queue):
        i,j,total,path=queue[cur]
        cur+=1
        if len(path)==3:
            candidate.append([total,path])
        else:
            for k in range(4):
                nx,ny = i+pxy[k][0], j+pxy[k][1]
                if 0<=nx<4 and 0<=ny<4:
                    if [nx,ny] not in path:
                        queue.append([nx, ny, total+sum(board[nx][ny]), path+[[nx, ny]]])
                    else:
                        queue.append([nx, ny, total, path+[[nx, ny]]])
    candidate.sort(key=lambda x:(-x[0]))
    return candidate[0][-1]

dxy = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
death_monster=[[0]*4 for _ in range(4)]
for _ in range(T):
    egg = [[item[:] for item in items] for items in board]
    new_board = [[item[:] for item in items] for items in board]
    for i in range(4):
        for j in range(4):
            for m in range(8):
                if board[i][j][m]==0:
                    continue
                for k in range(8):
                    nd = (m+k)%8
                    nx,ny = i+dxy[nd][0], j+dxy[nd][1]
                    if nx<0 or nx>=4 or ny<0 or ny>=4:
                        continue
                    if nx == pic_i and ny == pic_j:
                        continue
                    if death_monster[nx][ny]<0:
                        continue
                    new_board[i][j][m]-=board[i][j][m]
                    new_board[nx][ny][nd]+=board[i][j][m]
                    break
    board = new_board

    path = find_path()
    for k in range(3):
        x,y = path[k]
        if sum(board[x][y])>0:
            death_monster[x][y]=-3
            board[x][y]=[0]*8
    pic_i, pic_j = path[-1][0], path[-1][1]

    for i in range(4):
        for j in range(4):
            if death_monster[i][j]<0:
                death_monster[i][j]+=1

    for i in range(4):
        for j in range(4):
            for m in range(8):
                board[i][j][m]+=egg[i][j][m]

answer=0
for i in range(4):
    for j in range(4):
        answer+=sum(board[i][j])
print(answer)