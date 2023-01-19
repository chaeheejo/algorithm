N, K = map(int, input().split())
board = list(map(int, input().split()))
robot = [0]*N

answer=0
while True:
    answer+=1

    new_board = [0]*2*N
    new_robot = [0]*N
    for i in range(2*N):
        new_board[(i+1)%(N*2)] = board[i]
    for i in range(N-1):
        new_robot[(i+1)%N] = robot[i]
    board, robot = new_board, new_robot

    robot[-1]=0
    for i in range(N-2,-1,-1):
        if robot[i]==1 and robot[i+1]==0 and board[i+1]>=1:
            robot[i]=0
            robot[i+1]=1
            board[i+1]-=1

    if board[0]!=0 and robot[0]==0:
        robot[0]=1
        board[0] -= 1

    cnt_zero=0
    for i in range(2*N):
        if board[i]==0:
            cnt_zero+=1
    if cnt_zero>=K:
        break

print(answer)