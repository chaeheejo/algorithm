N, M, T = map(int, input().split())
disk = [list(map(int, input().split())) for _ in range(N)]
way_rotate = [list(map(int, input().split())) for _ in range(T)]

def rotate(d, k, array):
    if d==0:
        new = array[:]
        for _ in range(k):
            temp = new[:]
            for i in range(M):
                if i==M-1:
                    new[0]=temp[i]
                else:
                    new[i+1]=temp[i]
    else:
        new = array[:]
        for _ in range(k):
            temp = new[:]
            for i in range(M):
                if i==0:
                    new[-1]=temp[i]
                else:
                    new[i-1]=temp[i]
    return new

disk_adjacent=[[False] * N for _ in range(M)]
def check_value(a, b):
    i, j = a
    m, n = b
    if disk[i][j]==disk[m][n]:
        disk_adjacent[i][j]=True
        disk_adjacent[m][n]=True
        return True

def check():
    flag=True
    for i in range(N):
        for j in range(M):
            if disk_adjacent[i][j]:
                continue

            flag=False
            if j==0:
                check_value((i,j), (i,1))
                check_value((i,j), (i,-1))
            elif j==M-1:
                check_value((i,j), (i,-2))
            if i==0:
                check_value((i, j), (1, j))
            elif i==N-1:
                check_value((i, j), (N-2, j))

            if 0<=j+1<N:
                check_value((i,j), (i,j+1))
            if 0<=j-1<N:
                check_value((i,j), (i, j-1))
            if 0<=i+1<N:
                check_value((i, j), (i+1, j))
            if 0<=i-1<N:
                check_value((i, j), (i-1, j))

    if flag:
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if not disk_adjacent[i][j]:
                    total+=disk[i][j]
                    cnt+=1
        average = float(total)/float(cnt)

        for i in range(N):
            for j in range(M):
                if disk_adjacent[i][j]:
                    continue
                if disk[i][j]>average:
                    disk[i][j]-=1
                elif disk[i][j]<average:
                    disk[i][j]+=1


for t in range(T):
    x, d, k = way_rotate[t]

    for i in range(1,N+1):
        if i%x==0:
            disk[i-1] = rotate(d, k, disk[i-1])

    check()

answer=0
for i in range(N):
    for j in range(M):
        if not disk_adjacent[i][j]:
            answer+=disk[i][j]

print(answer)