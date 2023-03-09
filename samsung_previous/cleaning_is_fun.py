N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dxy = [(0,-1),(1,0),(0,1),(-1,0)]
def build_loc():
    loc,i,j,d=[],N//2,N//2,0
    now,total,flag=0,1,0
    while True:
        i,j = i+dxy[d][0],j+dxy[d][1]
        loc.append([i,j,d])
        now+=1
        if now==total:
            if flag==0:
                now,flag=0,1
            else:
                now,flag=0,0
                total+=1
            d=(d+1)%4
        if i==0 and j==0:
            break
    return loc

loc=build_loc()

clean_0 = [[0,0,2,0,0],[0,10,7,1,0],[5,99,0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
clean_1 = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,99,10,0],[0,0,5,0,0]]
clean_2 = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,99,5],[0,1,7,10,0],[0,0,2,0,0]]
clean_3 = [[0,0,5,0,0],[0,10,99,10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]
clean = [clean_0,clean_1,clean_2,clean_3]

answer=0
for i,j,d in loc:
    cmap = clean[d]
    a_sand=board[i][j]
    a_idx=[-1,-1]
    for n in range(5):
        nx = (i-2)+n
        for m in range(5):
            ny = (j-2)+m
            if cmap[n][m]==99:
                a_idx = [nx, ny]
            else:
                sand = int(board[i][j]*cmap[n][m]*0.01)
                if 0<=nx<N and 0<=ny<N:
                    board[nx][ny] += sand
                else:
                    answer += sand
                a_sand -= sand
    ax,ay = a_idx
    if 0<=ax<N and 0<=ay<N:
        board[ax][ay] += a_sand
    else:
        answer += a_sand
    board[i][j]=0

print(answer)