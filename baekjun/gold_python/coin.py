T = int(input())

answer=[]
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    total = int(input())
    dp = [0]*(total+1)
    dp[0]=1

    for c in coin:
        for i in range(total+1):
            if i>=c:
                dp[i]+=+dp[i-c]

    answer.append(dp[total])

for ans in answer:
    print(ans)