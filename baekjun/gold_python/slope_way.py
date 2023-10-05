N, L = map(int, input().split())
way = [list(map(int, input().split())) for _ in range(N)]

answer=0
def count_way(w):
    global answer

    for i in range(N-1):
        if abs(w[i]-w[i+1])>1:
            return
        if w[i]>w[i+1]:
            for k in range(L):
                if i+1+k >= N or w[i+1]!=w[i+1+k] or used[i+1+k]:
                    return
                if w[i+1]==w[i+1+k]:
                    used[i+1+k]=True
        elif w[i]<w[i+1]:
            for k in range(L):
                if i-k<0 or w[i]!=w[i-k] or used[i-k]:
                    return
                if w[i]==w[i-k]:
                    used[i-k]=True
    answer+=1

for w in way:
    used=[False]*N
    count_way(w)

for i in range(N):
    used = [False]*N
    count_way([w[i] for w in way])

print(answer)