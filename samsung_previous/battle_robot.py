N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

robot_info = [[0,0],[0,2]]
for i in range(N):
    for j in range(N):
        if board[i][j]==9:
            robot_info[0][0] = i
            robot_info[0][1] = j
            board[i][j]=0
            break

dxy = [(-1,0),(0,1),(1,0),(0,-1)]
def kill_monster(i,j):
    robot_level = robot_info[1][1]
    candidate = []
    queue=[[i,j]]
    cur=0
    visited=[[0]*N for _ in range(N)]
    visited[i][j]=1
    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]>robot_level:
                    visited[nx][ny]=1
                    continue
                queue.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1
                if board[nx][ny]>0 and board[nx][ny]<robot_level:
                    candidate.append([visited[nx][ny],nx,ny])
    candidate.sort(key=lambda x:(x[0],x[1],x[2]))
    if len(candidate)>0:
        time,x,y = candidate[0]
        board[x][y]=0
        return time-1,x,y
    else:
        return -1,-1,-1

answer=0
while True:
    time,i,j = kill_monster(robot_info[0][0],robot_info[0][1])
    if time==-1:
        break
    robot_info[0][0] = i
    robot_info[0][1] = j
    robot_info[1][0]+=1
    if robot_info[1][0]==robot_info[1][1]:
        robot_info[1][1]+=1
        robot_info[1][0]=0
    answer+=time
print(answer)