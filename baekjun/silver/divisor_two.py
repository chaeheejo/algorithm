def solution():
    n=int(input())
    answer=0

    for i in range(1,n+1):
        answer+=i*(n//i)

    print(answer)

if __name__ == '__main__':
    answer = solution()
