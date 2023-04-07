N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

group=[[] for _ in range(M)]
group_num =[[9]*N for _ in range(N)]
dxy = [(1,0),(0,1),(-1,0),(0,-1)]
def make_group(cnt,i,j):
    queue=[[i,j]]
    cur=0
    group_num[i][j]=cnt
    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        for k in range(4):
            nx,ny = x+dxy[k][0],y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]==0:
                    visited[nx][ny]=1
                    continue
                if board[nx][ny]==board[x][y] or board[nx][ny]==board[x][y]+1:
                    queue.append([nx,ny])
                    group_num[nx][ny]=cnt
                    visited[nx][ny]=1
    group[cnt].extend(queue)

visited=[[0]*N for _ in range(N)]
group_cnt=0
for i in range(N):
    for j in range(N):
        if board[i][j]==1 and visited[i][j]==0:
            visited[i][j]=1
            make_group(group_cnt,i,j)
            group_cnt+=1

def follow_head(i,j):
    global board
    new_board = [b[:] for b in board]
    num = group_num[i][j]
    for k in range(len(group[num])):
        x,y = group[num][k]
        px,py = group[num][k-1]
        new_board[px][py] = board[x][y]
    board = new_board
    hi,hj = group[num].pop()
    group[num].insert(0,[hi,hj])

def change_head_and_tail(i,j):
    new_group=[]
    idx,rtn = 0,0
    num = group_num[i][j]
    for k in range(len(group[num])):
        x,y = group[num][k]
        if x==i and y==j:
            rtn=k+1
        if board[x][y]==3:
            board[x][y]=1
            board[group[num][0][0]][group[num][0][1]]=3
            idx = k
            break
    while len(new_group)<len(group[num]):
        new_group.append(group[num][idx])
        idx = (idx-1)%len(group[num])
    group[num] = new_group
    return rtn

answer=0
si,sj,sd = 0,0,0
for d in range(K):
    for m in range(M):
        follow_head(group[m][0][0],group[m][0][1])
    ri,rj = si,sj
    while 0<=ri<N and 0<=rj<N:
        if 0<board[ri][rj]<4:
            score = change_head_and_tail(ri,rj)
            answer+=score*score
            break
        ri+=dxy[(sd+1)%4][0]
        rj+=dxy[(sd+1)%4][1]
    if si+dxy[sd][0]<0 or si+dxy[sd][0]>=N or sj+dxy[sd][1]<0 or sj+dxy[sd][1]>=N:
        sd = (sd+1)%4
    else:
        si+=dxy[sd][0]
        sj+=dxy[sd][1]
print(answer)