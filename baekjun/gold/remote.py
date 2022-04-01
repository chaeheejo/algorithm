from itertools import product

def solution():
    channel=int(input())
    n=int(input())
    cannotUseNum=[]
    if n!=0:
        cannotUseNum=list(input().split())
    canUseNum=[str(e) for e in range(10) if str(e) not in cannotUseNum]
    answer=[]

    for i in range(1,7):
        tempList = list(product(canUseNum, repeat=i))
        for temp in tempList:
            num = ''.join(temp)
            answer.append(len(num)+abs(channel-int(num)))
    answer.append(abs(channel-100))
    return min(answer)


if __name__ == '__main__':
    answer = solution()
    print(answer)