A, B = map(int, input().split())
N, M = map(int, input().split())

robot_direction = {}
robot = [[]]
board = [[0]*A for _ in range(B)]
for k in range(1,N+1):
    j,i,d = input().split()
    i,j = B-int(i),int(j)-1
    board[i][j] = k
    robot.append([i,j])

    if d=='E':
        robot_direction[k] = 0
    elif d=='N':
        robot_direction[k] = 1
    elif d=='W':
        robot_direction[k] = 2
    else:
        robot_direction[k] = 3

command=[list(input().split()) for _ in range(M)]
dxy = [(0,1),(-1,0),(0,-1),(1,0)]
def move_robot():
    for m in range(M):
        r,c,k = command[m]
        r,k = int(r),int(k)

        if c=='L':
            for _ in range(k):
                robot_direction[r] = (robot_direction[r] + 1) % 4
        elif c=='R':
            for _ in range(k):
                robot_direction[r] = (robot_direction[r] - 1) % 4
        else:
            x,y = robot[r]
            for _ in range(k):
                x += dxy[robot_direction[r]][0]
                y += dxy[robot_direction[r]][1]
                if 0<=x<B and 0<=y<A:
                    if board[x][y]!=0:
                        return 'Robot '+str(r)+' crashes into robot '+str(board[x][y])
                else:
                    return 'Robot '+str(r)+' crashes into the wall'
            i,j = robot[r]
            board[i][j]=0
            board[x][y]=r
            robot[r] = [x,y]
    return 'OK'

print(move_robot())