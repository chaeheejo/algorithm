N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(len(items)+1)]
for i in range(len(items) + 1):
    for weight in range(K + 1):
        if i==0 or weight==0:
            dp[i][weight]=0
        elif items[i-1][0]<=weight:
            dp[i][weight] = max(dp[i-1][weight], items[i-1][1]+dp[i-1][weight-items[i-1][0]])
        else:
            dp[i][weight] = dp[i-1][weight]

print(dp[len(items)][K])