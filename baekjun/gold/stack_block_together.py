N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(H+1)

for block in blocks:
    for goal in range(H, 0, -1):
        for b in block:
            if goal+b<=H and dp[goal]!=0:
                dp[goal+b]+=dp[goal]
    for b in block:
        dp[b]+=1

print(dp[H]%10007)