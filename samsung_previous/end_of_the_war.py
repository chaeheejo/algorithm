N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def cnt_people(square):
    village = [[-1]*N for _ in range(N)]
    people=[0,0,0,0,0]

    for k in range(4):
        i,j = square[k]
        while True:
            village[i][j]=0
            i+=dxy[k][0]
            j+=dxy[k][1]
            if i==square[(k+1)%4][0] and j==square[(k+1)%4][1]:
                break

    for i in range(N):
        flag=0
        for j in range(N):
            if i==square[1][0] and j==square[1][1]:
                continue
            if i==square[3][0] and j==square[3][1]:
                continue
            if village[i][j]==0:
                flag = ~flag
            else:
                if flag:
                    village[i][j]=0

    for i in range(N):
        for j in range(N):
            if village[i][j]==0:
                continue
            if i<square[0][0] and j<=square[1][1]:
                village[i][j]=1
            elif i<=square[2][0] and j>square[1][1]:
                village[i][j]=2
            elif square[0][0]<=i and j<square[3][1]:
                village[i][j]=3
            elif square[2][0]<i and j>=square[3][1]:
                village[i][j]=4

    for i in range(square[1][0],square[3][0]):
        for j in range(square[0][1],square[2][1]):
            if village[i][j+1]==0:
                break
            if village[i][j]!=village[i][j+1]:
                village[i][j+1]=village[i][j]
        for j in range(square[2][1],square[0][1],-1):
            if village[i][j-1]==0:
                break
            if village[i][j]!=village[i][j-1]:
                village[i][j-1]=village[i][j]

    for i in range(N):
        for j in range(N):
            people[village[i][j]]+=board[i][j]

    max_num,min_num = max(people),min(people)
    return max_num-min_num

def is_square(i,j,t,s):
    while 0<=t<N and 0<=s<N:
        if t==i and s==j:
            return True
        t += dxy[3][0]
        s += dxy[3][1]
    return False

answer=9999
dxy = [(-1,1),(1,1),(1,-1),(-1,-1)]
for i in range(N):
    for j in range(N):
        x, y = i+dxy[0][0], j+dxy[0][1]
        while 0<=x<N and 0<=y<N:
            n, m = x+dxy[1][0], y+dxy[1][1]
            while 0<=n<N and 0<=m<N:
                t, s = n+dxy[2][0], m+dxy[2][1]
                while 0<=t<N and 0<=s<N:
                    if is_square(i,j,t,s):
                        square=[[i,j],[x,y],[n,m],[t,s]]
                        answer = min(answer,cnt_people(square))
                    t += dxy[2][0]
                    s += dxy[2][1]
                n += dxy[1][0]
                m += dxy[1][1]
            x += dxy[0][0]
            y += dxy[0][1]
print(answer)