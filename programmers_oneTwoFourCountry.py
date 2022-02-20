def solution(n):
    answer = ''

    res = (1,2,4)
    while (n>0):
        n-=1
        answer = str(res[n % 3]) + answer
        n//=3

    return answer
