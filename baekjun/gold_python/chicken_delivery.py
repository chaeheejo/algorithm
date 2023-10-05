N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def combination(arr,r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], r-1):
                yield [arr[i]]+next

def find_chicken_distance(chosen_chicken):
    total=0
    for hi,hj in home:
        distance = 9999
        for i in chosen_chicken:
            distance = min(distance,abs(hi-chicken[i][0])+abs(hj-chicken[i][1]))
        total+=distance
    return total

chicken, home = [],[]
for i in range(N):
    for j in range(N):
        if board[i][j]==2:
            chicken.append((i,j))
        elif board[i][j]==1:
            home.append((i,j))

answer=9999
if len(chicken)-M==0:
    answer = find_chicken_distance(list(range(len(chicken))))
else:
    for comb in combination(list(range(len(chicken))), M):
        answer = min(answer, find_chicken_distance(comb))
print(answer)