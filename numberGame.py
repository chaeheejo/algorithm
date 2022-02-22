#이것이 코딩 테스트다 Q3

def numberGame(n,m,array):
    answer=0
    for i in range(n):
        array[i].sort()
        answer=max(answer,array[i][0])
    return answer

if __name__ == '__main__':
    n=[[7,3,1,8],[3,3,3,4]]
    answer = numberGame(2,4,n)
    print(answer)
