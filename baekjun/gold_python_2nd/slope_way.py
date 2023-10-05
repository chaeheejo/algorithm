N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def cnt_way(way):
    global answer
    for i in range(N-1):
        if way[i]-way[i+1]==1:
            for k in range(L):
                if i+1+k<N and way[i+1]==way[i+1+k] and slope[i+1+k]==0:
                    slope[i+1+k]=1
                else:
                    return
        elif way[i]-way[i+1]==-1:
            for k in range(L):
                if i-k>=0 and way[i]==way[i-k] and slope[i-k]==0:
                    slope[i-k]=1
                else:
                    return
        elif way[i]==way[i+1]:
            continue
        else:
            return
    answer+=1

answer=0
for b in board:
    slope=[0]*N
    cnt_way(b)

for i in range(N):
    slope = [0]*N
    cnt_way([b[i] for b in board])
print(answer)