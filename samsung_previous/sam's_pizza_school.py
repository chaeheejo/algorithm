N, K = map(int, input().split())
board = list(map(int, input().split()))

def roll_dough():
    global board
    rolled = [[board[0]], [board[1]]]
    before_rolled = board[2:]
    while True:
        tmp_r = list(zip(*rolled[::-1]))
        if len(before_rolled)-len(tmp_r[0])<0:
            break
        rolled = tmp_r + [before_rolled[:len(tmp_r[0])]]
        before_rolled = before_rolled[len(rolled[0]):]

    board = []
    for i in range(len(rolled)):
        tmp = list(rolled[i])
        if i == len(rolled) - 1:
            tmp += before_rolled
        board.append(tmp)

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def push_dough():
    global board
    pushed=[[0]*len(board[-1]) for _ in range(len(board))]
    visited = [[False]*len(board[-1]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            pushed[i][j]+=board[i][j]
            visited[i][j]=True
            for k in range(4):
                nx,ny = i+dxy[k][0], j+dxy[k][1]
                if 0<=nx<len(board) and 0<=ny<len(board[nx]) and visited[nx][ny]==False:
                    d = abs(board[i][j]-board[nx][ny])//5
                    if board[i][j]>board[nx][ny]:
                        pushed[i][j]-=d
                        pushed[nx][ny]+=d
                    elif board[nx][ny]>board[i][j]:
                        pushed[nx][ny]-=d
                        pushed[i][j]+=d

    push_board = list(zip(*pushed[::-1]))
    board=[]
    for i in range(len(push_board)):
        for j in range(len(push_board[i])):
            if push_board[i][j]!=0:
                board.append(push_board[i][j])

def fold_dough():
    global board
    one_fold = [[]]
    for i in range(N//2-1,-1,-1):
        one_fold[0].append(board[i])
    one_fold.append(board[N // 2:])
    board = one_fold

    two_fold_left = [item[:N//2//2] for item in board]
    two_fold_right = [item[N//2//2:] for item in board]
    two_fold_left = list(zip(*two_fold_left[::-1]))
    two_fold_left = list(zip(*two_fold_left[::-1]))
    board = []
    for i in range(2):
        tmp = []
        for j in range(N//2//2):
            tmp.append(two_fold_left[i][j])
        board.append(tmp)
    for i in range(2):
        tmp = []
        for j in range(N//2//2):
            tmp.append(two_fold_right[i][j])
        board.append(tmp)

answer=0
while True:
    min_value = min(board)
    while min_value in board:
        min_idx = board.index(min_value)
        board[min_idx]+=1

    roll_dough()
    push_dough()
    fold_dough()
    push_dough()

    answer+=1
    if max(board)-min(board)<=K:
        break

print(answer)