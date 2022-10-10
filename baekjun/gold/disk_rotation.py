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

def check_value(a, b):
    i, j = a
    m, n = b
    if disk[i][j]!='x' and disk[i][j]==disk[m][n]:
        disk_adjacent[i][j]=True
        disk_adjacent[m][n]=True
        return True
    else:
        return False

def check_adjacent():
    flag=[]
    for i in range(N):
        for j in range(M):
            if j==0:
                flag.append(check_value((i,j), (i,1)))
                flag.append(check_value((i,j), (i,-1)))
            elif j==M-1:
                flag.append(check_value((i, j), (i, 0)))
                flag.append(check_value((i,j), (i,-2)))
            if i==0:
                flag.append(check_value((i, j), (1, j)))
            elif i==N-1:
                flag.append(check_value((i, j), (N-2, j)))

            if 0<=j+1<M:
                flag.append(check_value((i,j), (i,j+1)))
            if 0<=j-1<M:
                flag.append(check_value((i,j), (i, j-1)))
            if 0<=i+1<N:
                flag.append(check_value((i, j), (i+1, j)))
            if 0<=i-1<N:
                flag.append(check_value((i, j), (i-1, j)))

    if True in flag:
        for i in range(N):
            for j in range(M):
                if disk_adjacent[i][j]:
                    disk[i][j]='x'
    else:
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if disk[i][j]!='x':
                    total+=disk[i][j]
                    cnt+=1
        if cnt==0:
            return
        average = float(total)/float(cnt)

        for i in range(N):
            for j in range(M):
                if disk[i][j]=='x':
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
    disk_adjacent = [[False] * M for _ in range(N)]
    check_adjacent()

answer=0
for i in range(N):
    for j in range(M):
        if disk[i][j]!='x':
            answer+=disk[i][j]

print(answer)