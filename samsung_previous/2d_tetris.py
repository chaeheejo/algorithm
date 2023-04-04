K = int(input())
cmd = [list(map(int, input().split())) for _ in range(K)]

rboard = [[0]*4 for _ in range(6)]
yboard = [[0]*4 for _ in range(6)]

def make_block(board,t,y):
    if t==1 or t==3:
        nx=0
        while nx+1<6 and board[nx+1][y]==0:
            nx+=1
        board[nx][y]=1
        if t==3:
            board[nx-1][y]=1
    else:
        nx=0
        while nx+1<6 and board[nx+1][y]==0 and board[nx+1][y+1]==0:
            nx+=1
        board[nx][y]=1
        board[nx][y+1]=1

def remove_block(board,idx):
    for i in range(idx,0,-1):
        for j in range(4):
            board[i][j] = board[i-1][j]
    for j in range(4):
        board[0][j] = 0

def get_score(board):
    score,blank,i=0,0,5
    while i>1:
        cnt = board[i].count(1)
        if cnt==4:
            score+=1
            remove_block(board,i)
            i+=1
        i-=1
    return score

def push_block(board):
    for i in range(2):
        for j in range(4):
            if board[i][j]:
                remove_block(board,5)
                break

score=0
for t,x,y in cmd:
    make_block(yboard,t,y)
    if t==2:
        make_block(rboard,3,3-x)
    elif t==3:
        make_block(rboard,2,3-x-1)
    else:
        make_block(rboard,1,3-x)

    score+=get_score(rboard)
    score+=get_score(yboard)

    push_block(rboard)
    push_block(yboard)

print(score)

block=0
for b in rboard:
    block+=sum(b)
for b in yboard:
    block+=sum(b)
print(block)