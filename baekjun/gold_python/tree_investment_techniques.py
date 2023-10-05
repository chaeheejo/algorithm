N, M, K = map(int, input().split())
nutrient = [list(map(int, input().split())) for _ in range(N)]
board = [[5]*N for _ in range(N)]
tree_loc = [list(map(int, input().split())) for _ in range(M)]
tree = [[[] for _ in range(N)] for _ in range(N)]

for i,j,z in tree_loc:
    tree[i-1][j-1].append(z)

def spring():
    for i in range(N):
        for j in range(N):
            if not tree[i][j]:
                continue

            tmp=[]
            tree[i][j].sort()

            for t in range(len(tree[i][j])):
                if board[i][j]-tree[i][j][t]>=0:
                    board[i][j]-=tree[i][j][t]
                    tree[i][j][t]+=1
                else:
                    tmp = tree[i][j][t:]
                    tree[i][j] = tree[i][j][:t]
                    break

            summer(i,j,tmp)

def summer(i,j,dead_tree):
    for dt in dead_tree:
        board[i][j] += int(dt/2)

dxy = [(-1,-1),(1,1),(-1,1),(1,-1),(1,0),(-1,0),(0,1),(0,-1)]
def fall():
    for i in range(N):
        for j in range(N):
            if not tree[i][j]:
                continue

            for t in range(len(tree[i][j])):
                if tree[i][j][t]%5==0:
                    for k in range(8):
                        nx,ny = i+dxy[k][0], j+dxy[k][1]
                        if 0<=nx<N and 0<=ny<N:
                            tree[nx][ny].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            board[i][j] += nutrient[i][j]

for _ in range(K):
    spring()
    fall()
    winter()

answer=0
for i in range(N):
    for j in range(N):
        if not tree[i][j]:
            continue
        answer+=len(tree[i][j])
print(answer)