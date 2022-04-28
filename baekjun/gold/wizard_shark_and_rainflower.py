n,m = list(map(int, input().split()))
water = [list(map(int, input().split())) for _ in range(n)]
dist = [list(map(int, input().split())) for _ in range(m)]
movement = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

def addDiagonal(x, y):
    dia =[(-1,-1),(-1,1),(1,1),(1,-1)]
    cnt=0
    for d in dia:
        i = x+d[0]
        j = y+d[1]
        if 0<=i<n and 0<=j<n and water[i][j]>0:
            cnt+=1
    return cnt

def moveCloud(d, s, old):
    new =[]

    while old:
        new_x, new_y = 0,0
        new_x = old[0][0]+movement[d-1][0]*s
        new_y = old[0][1]+movement[d-1][1]*s

        while new_x<0:
            new_x+=n
        while new_x>=n:
            new_x-=n
        while new_y<0:
            new_y+=n
        while new_y>=n:
            new_y-=n
        new.append((new_x, new_y))
        old.remove((old[0][0], old[0][1]))
    return new

cloud = []
cloud.append((n-1,0))
cloud.append((n-1,1))
cloud.append((n-2,0))
cloud.append((n-2,1))
for k in range(m):
    d, s = dist[k]
    cloud = moveCloud(d,s, cloud)

    for i, j in cloud:
        water[i][j]+=1
    for i, j in cloud:
        water[i][j]+=addDiagonal(i,j)

    new_cloud=[]
    for i in range(n):
        for j in range(n):
            if water[i][j]>1 and (i,j) not in cloud:
                water[i][j]-=2
                new_cloud.append((i,j))
    cloud=new_cloud

answer=0
for i in range(n):
    for j in range(n):
        answer+=water[i][j]
print(answer)