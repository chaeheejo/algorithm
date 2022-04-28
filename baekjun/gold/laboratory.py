def bfs(virusMap):
    queue = []
    bfsMap=[[0]*len(virusMap[0]) for _ in range(len(virusMap))]
    xdirect = [1,-1,0,0]
    ydirect = [0,0,1,-1]
    cur =0

    for i in range(len(virusMap)):
        for j in range(len(virusMap[0])):
            bfsMap[i][j] = virusMap[i][j]
            if bfsMap[i][j]==2:
                queue.append((i,j))

    while cur < len(queue):
        i, j = queue[cur]
        cur+=1
        for k in range(4):
            tmpI,tmpJ = i+ xdirect[k], j+ ydirect[k]
            if 0<= tmpI <len(bfsMap) and 0<= tmpJ <len(bfsMap[0]) and bfsMap[tmpI][tmpJ]==0:
                bfsMap[tmpI][tmpJ]=2
                queue.append((tmpI, tmpJ))

    cnt=0
    for i in range(len(bfsMap)):
        for j in range(len(bfsMap[0])):
            if bfsMap[i][j]==0:
                cnt+=1

    return cnt

n, m = map(int, input().split(' '))
virusMap = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for w1x in range(n):
    for w1y in range(m):
        if virusMap[w1x][w1y] == 0:
            for w2x in range(n):
                for w2y in range(m):
                    if virusMap[w2x][w2y] == 0:
                        for w3x in range(n):
                            for w3y in range(m):
                                if virusMap[w3x][w3y]==0:
                                    if w1x == w2x and w1y == w2y:
                                        continue
                                    if w2x == w3x and w2y == w3y:
                                        continue
                                    if w1x == w3x and w1y == w3y:
                                        continue
                                    virusMap[w1x][w1y] =1
                                    virusMap[w2x][w2y] =1
                                    virusMap[w3x][w3y] =1

                                    cnt = max(cnt,bfs(virusMap))

                                    virusMap[w1x][w1y] = 0
                                    virusMap[w2x][w2y] = 0
                                    virusMap[w3x][w3y] = 0
print(cnt)