N, M, Q = map(int, input().split())
dart = [list(map(int, input().split())) for _ in range(N)]
spin = [list(map(int, input().split())) for _ in range(Q)]

def spin_dart(x,d,k):
    for i in range(N):
        if (i+1)%x==0:
            new = [0]*M
            if d==0:
                for j in range(M):
                    new[(j+k)%M] = dart[i][j]
                dart[i] = new
            else:
                for j in range(M):
                    new[(j-k)%M] = dart[i][j]
                dart[i] = new

def remove_number():
    flag=0
    check = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if dart[i][j]==-1:
                continue

            if dart[i][j]==dart[i][(j-1)%M]:
                check[i][j]=check[i][(j-1)%M]=flag=1
            if dart[i][j]==dart[i][(j+1)%M]:
                check[i][j]=check[i][(j+1)%M]=flag=1

            if i==0:
                if dart[0][j]==dart[1][j]:
                    check[0][j]=check[1][j]=flag=1
            elif i==N-1:
                if dart[N-1][j]==dart[N-2][j]:
                    check[N-1][j]=check[N-1][j]=flag=1
            else:
                if dart[i][j]==dart[i-1][j]:
                    check[i][j]=check[i-1][j]=flag=1
                if dart[i][j]==dart[i+1][j]:
                    check[i][j]=check[i+1][j]=flag=1

    if flag:
        for i in range(N):
            for j in range(M):
                if check[i][j]:
                    dart[i][j] = -1
    else:
        normalize()

def normalize():
    mean,total = 0,0
    for i in range(N):
        for j in range(M):
            if dart[i][j]!=-1:
                total+=dart[i][j]
                mean+=1
    mean = total//mean

    for i in range(N):
        for j in range(M):
            if dart[i][j]!=-1:
                if dart[i][j]>mean:
                    dart[i][j]-=1
                elif dart[i][j]<mean:
                    dart[i][j]+=1

for x,d,k in spin:
    spin_dart(x,d,k)
    remove_number()

answer=0
for i in range(N):
    for j in range(M):
        if dart[i][j]!=-1:
            answer+=dart[i][j]
print(answer)