H, M, N = map(int, input().split())
ladder=[]
if M>0:
    ladder = [list(map(int, input().split())) for _ in range(M)]
board = [[0]*H for _ in range(N)]

for i,j in ladder:
    board[i-1][j-1] = 2
    board[i-1][j] = 1

empty=[]
for i in range(N):
    for j in range(H):
        if board[i][j]==0:
            empty.append([i,j])

def play_game():
    for k in range(H):
        i,j=0,k
        flag=0
        while 0<=i<N and 0<=j<H:
            if board[i][j]==1 and flag==0:
                flag=1
                j-=1
            elif board[i][j]==2 and flag==0:
                flag=1
                j+=1
            else:
                flag=0
                i+=1
        if j!=k:
            return False
    return True

def change_right(i, j):
    if j+1<H and board[i][j]==0 and board[i][j+1]==0:
        board[i][j], board[i][j+1]=2,1
        return True
    return False

def undo(i,j):
    board[i][j], board[i][j+1]=0,0

def plus_labber():
    global answer
    if play_game():
        answer = 0
        return
    for n in range(len(empty)):
        i,j = empty[n]
        if change_right(i, j):
            if play_game():
                answer = min(answer,1)
            for m in range(n+1,len(empty)):
                x,y = empty[m]
                if change_right(x, y):
                    if play_game():
                        answer = min(answer,2)
                    for k in range(m+1, len(empty)):
                        nx,ny = empty[k]
                        if change_right(nx, ny):
                            if play_game():
                                answer = min(answer,3)
                            undo(nx,ny)
                    undo(x,y)
            undo(i,j)

answer=9999
plus_labber()
if answer==9999:
    answer=-1
print(answer)