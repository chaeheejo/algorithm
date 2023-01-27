N = int(input())
M = int(input())

broken=[]
if M!=0:
    broken = list(map(int, input().split()))

answer=[abs(100-N)]

def permutation(array,r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in permutation(array,r-1):
                yield [array[i]]+next

btn = [str(i) for i in range(10) if i not in broken]
for i in range(6):
    for per in permutation(btn,i+1):
        num = int(''.join(per))
        answer.append(len(per)+abs(num-N))
print(min(answer))
