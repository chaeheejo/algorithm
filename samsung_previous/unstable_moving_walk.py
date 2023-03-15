N, K = map(int, input().split())
safety = list(map(int, input().split()))
people = [0]*(2*N)

answer=0
while True:
    safety.insert(0,safety.pop())
    people.insert(0,people.pop())
    people[N-1]=0

    for i in range(N-2,-1,-1):
        if people[i]==1 and people[i+1]==0 and safety[i+1]>0:
            people[i]=0
            people[i+1]=1
            safety[i+1]-=1
    people[N-1]=0

    if people[0]==0 and safety[0]>0:
        people[0]=1
        safety[0]-=1

    answer+=1
    tmp=0
    for i in range(2*N):
        if safety[i]==0:
            tmp+=1
    if tmp>=K:
        break
print(answer)