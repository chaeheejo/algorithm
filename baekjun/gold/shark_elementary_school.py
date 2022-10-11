N = int(input())
like = [list(map(int, input().split())) for _ in range(N*N)]
seat = [[0]*N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check_adjacent(condition):
    maximum = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                tmpI, tmpJ = i + dx[k], j + dy[k]
                if 0 > tmpI or tmpI >= N or 0 > tmpJ or tmpJ >= N:
                    continue
                if seat[tmpI][tmpJ] in condition:
                    probability[i][j] += 1

                    if probability[i][j] > maximum:
                        maximum = probability[i][j]
    return maximum

for k in range(N):
    n, a, b, c, d = like[k]
    probability=[[0]*N for _ in range(N)]

    maximum=check_adjacent([a,b,c,d])

    candidate=[]
    for i in range(N):
        for j in range(N):
            if maximum==probability[i][j]:
                candidate.append((i,j))

    if len(candidate)==1:
        i, j = candidate[0]
        seat[i][j]=n
        continue

    probability = [[0] * N for _ in range(N)]
    maximum = check_adjacent([0])

    candidate = []
    for i in range(N):
        for j in range(N):
            if maximum == probability[i][j]:
                candidate.append((i, j))

    if len(candidate)==1:
        i, j = candidate[0]
        seat[i][j]=n
        continue

    minimumI=999
    for i,j in candidate:
        if minimumI>i:
            minimumI=i

    cnt=0
    cndI, cndJ = 0,0
    for i, j in candidate:
        if minimumI==i:
            cnt+=1
            cndI, cndJ = i, j

    if cnt==1:
        seat[cndI][cndJ]=n

    minimumJ = 999
    for i, j in candidate:
        if minimumJ>j:
            minimumJ=j

    cndI, cndJ = 0, 0
    for i, j in candidate:
        if minimumJ == j:
            cndI, cndJ = i, j

    seat[cndI][cndJ]=n

for j in range(N):
    for k in range(4):
        tmpI, tmpJ = dx[k], j + dy[k]
        if 0 > tmpI or tmpI >= N or 0 > tmpJ or tmpJ >= N:
            continue
        if seat[tmpI][tmpJ] in like[]