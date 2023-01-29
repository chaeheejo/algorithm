N = int(input())
board = [[0]*N for _ in range(N)]

blank,teacher=[],[]
for i in range(N):
    b = list(input().split())
    for j in range(N):
        if b[j]=='T':
            board[i][j]=-1
            teacher.append([i,j])
        elif b[j]=='S':
            board[i][j]=1
        else:
            blank.append([i,j])

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def check_surveillance():
    for ti,tj in teacher:
        for k in range(4):
            nx,ny = ti+dxy[k][0], tj+dxy[k][1]
            while 0<=nx<N and 0<=ny<N:
                if board[nx][ny]==1:
                    return False
                elif board[nx][ny]==2:
                    break
                nx += dxy[k][0]
                ny += dxy[k][1]
    return True

def combination(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:],r-1):
                yield [array[i]]+next

answer='NO'
for com in combination(range(len(blank)),3):
    for c in com:
        i,j = blank[c]
        board[i][j]=2

    if check_surveillance():
        answer='YES'
        break

    for c in com:
        i,j = blank[c]
        board[i][j]=0

print(answer)