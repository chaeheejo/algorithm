N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def make_group(i,j):
    queue=[[i,j]]
    cur=0
    visited=[[0]*N for _ in range(N)]

    while cur<len(queue):
        x,y = queue[cur]
        cur+=1
        visited[x][y]=1

        for k in range(4):
            nx,ny = x+dxy[k][0], y+dxy[k][1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if board[nx][ny]==board[i][j]:
                    queue.append([nx,ny])
                visited[nx][ny]=1
    return queue

def get_score():
    score=0
    group=[]

    is_group = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not is_group[i][j]:
                tmp = make_group(i,j)
                group.append(tmp)

                for x,y in tmp:
                    is_group[x][y] = True

    for one in range(len(group)):
        for two in range(one+1,len(group)):
            search,at = one,two
            if len(group[two])<len(group[one]):
                search,at = two, one

            value_s, value_a = board[group[search][0][0]][group[search][0][1]], board[group[at][0][0]][group[at][0][1]]
            neighbor = 0

            for x,y in group[search]:
                for k in range(4):
                    nx,ny = x+dxy[k][0], y+dxy[k][1]
                    if 0<=nx<N and 0<=ny<N and board[nx][ny]==value_a:
                        if [nx,ny] in group[at]:
                            neighbor+=1
            score+=((len(group[search])+len(group[at]))*value_s*value_a*neighbor)
    return score

def rotate_middle():
    new_board = [item[:] for item in board]
    for i in range(N):
        new_board[N//2][i] = board[i][N//2]
        new_board[N-1-i][N//2] = board[N//2][i]
    return new_board

def rotate_square():
    new_board = [item[:] for item in board]
    for i in range(N):
        if i<N//2:
            tmp=[]
            for j in range(N//2):
                tmp.append(board[i][j])
            for x in range(N//2):
                new_board[x][N//2-1-i] = tmp[x]
            tmp=[]
            for j in range(N//2+1,N):
                tmp.append(board[i][j])
            for x in range(N//2):
                new_board[x][N-1-i] = tmp[x]
        elif N//2<i<N:
            tmp = []
            for j in range(N//2):
                tmp.append(board[i][j])
            for x in range(N//2):
                new_board[x+N//2+1][N//2-1-(i-(N//2+1))] = tmp[x]
            tmp=[]
            for j in range(N//2+1, N):
                tmp.append(board[i][j])
            for x in range(N//2):
                new_board[x+N//2+1][N-1-(i-(N//2+1))] = tmp[x]
    return new_board

answer=get_score()
for _ in range(3):
    board = rotate_middle()
    board = rotate_square()
    answer += get_score()
print(answer)