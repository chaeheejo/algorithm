N, L = map(int, input().split())

way = []
for _ in range(N):
    way.append(list(map(int, input().split())))

answer=0
def count_way(w):
    global answer
    maximum = max(w)
    cnt = w.count(maximum)
    less = w.count(maximum-1)
    more = w.count(maximum+1)

    if cnt==N:
        answer+=1
        print(w, 1)
    else:
        left = -1
        right = -1
        if less>0 and more==0:
            for i in range(len(w)):
                if w[i]==maximum-1:
                    if left==-1:
                        left=i
                        right=i
                    else:
                        right=i
                else:
                    if right-left+2>L and (left==0 or right==N-1):
                        answer+=1
                        print(w, 2)
                    left=-1
                    right=-1

        elif less==0 and more>0:
            for i in range(len(w)):
                if w[i]==maximum+1:
                    if left==-1:
                        left=i
                        right=i
                    else:
                        right=i
                else:
                    if right-left+2>L and (left==0 or right==N-1):
                        answer+=1
                        print(w, 3)
                    left=-1
                    right=-1

for w in way:
    count_way(w)

for i in range(N):
    count_way([w[i] for w in way])

print(answer)