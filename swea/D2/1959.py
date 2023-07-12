T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N>M:
        A,B = B,A
        N,M = M,N

    answer=0
    for x in range(M-N+1):
        cur = 0
        for i in range(N):
            cur+=A[i]*B[x+i]
        answer = max(answer, cur)

    print('#%d %d' % (t+1, answer))