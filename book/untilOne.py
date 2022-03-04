#이것이 코딩테스트다 Q4

def untilOne(n,k):
    answer=0
    while n>1:
        if n%k==0:
            n/=k
        else:
            n-=1
        answer+=1

    return answer

if __name__ == '__main__':
    answer = untilOne(25,3)
    print(answer)
