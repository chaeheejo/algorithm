N, M, K = map(int, input().split())
atomic = []
for _ in range(M):
    i,j,m,s,d = map(int, input().split())
    atomic.append([i-1,j-1,m,s,d])

board = [[[] for _ in range(N)] for _ in range(N)]
dxy = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
for _ in range(K):
    while atomic:
        i,j,m,s,d = atomic.pop()
        nx,ny = (i+dxy[d][0]*s)%N, (j+dxy[d][1]*s)%N
        board[nx][ny].append([m,s,d])

    for i in range(N):
        for j in range(N):
            if len(board[i][j])>1:
                length = len(board[i][j])
                tm,ts,d_even,d_odd = 0,0,0,0

                while board[i][j]:
                    m,s,d = board[i][j].pop()
                    tm+=m
                    ts+=s
                    if d%2==0:
                        d_even+=1
                    else:
                        d_odd+=1
                tm//=5
                ts//=length

                if tm>0:
                    drc=[]
                    if d_even==length or d_odd==length:
                        drc=[0,2,4,6]
                    else:
                        drc=[1,3,5,7]
                    for k in range(4):
                        atomic.append([i,j,tm,ts,drc[k]])

            elif len(board[i][j])==1:
                m,s,d = board[i][j].pop()
                atomic.append([i,j,m,s,d])

answer=0
for _,_,m,_,_ in atomic:
    answer+=m
print(answer)