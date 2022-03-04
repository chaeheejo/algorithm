#이것이 코딩 테스트다 그리디 Q2

def bigNumber(n, m, k):
    total=0
    n.sort()
    cnt=0

    while cnt<m:
        for i in range(k):
            if cnt<m:
                total += n[-1]
                cnt+=1
        if cnt < m:
            total+=n[-2]
            cnt+=1

    return total

if __name__ == '__main__':
    n=[3,4,3,4,3]
    answer = bigNumber(n,7,2)
    print(answer)
