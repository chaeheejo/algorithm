def bfs(n,r1,c1,r2,c2):
    cnt=-1
    queue = [(r1,c1,0)]
    xdirect = [2,2,-2,-2,0,0]
    ydirect = [1,-1,1,-1,2,-2]
    visited = [[-1]*n for _ in range(n)]
    cur=0

    while cur< len(queue):
        i,j,g = queue[cur]
        cur+=1
        if i==r2 and j==c2:
            cnt=g
            break

        for k in range(6):
            tmpI, tmpJ = i + xdirect[k], j + ydirect[k]
            if 0<= tmpI <n and 0<= tmpJ <n and visited[tmpI][tmpJ]==-1:
                queue.append((tmpI, tmpJ,g+1))
                visited[tmpI][tmpJ] = 0

    return cnt

n = int(input())
r1,c1,r2,c2 = list(map(int, input().split()))

print(bfs(n,r1,c1,r2,c2))