def solution():
    n = int(input())
    day = [[0,0] for _ in range(n)]
    dp = [0 for _ in range(n+1)]

    for i in range(n):
        time, money = [int(v) for v in input().split(' ')]
        day[i][0] = time
        day[i][1] = money

    for i in range(n):
        dp[i + 1] = max(dp[i + 1], dp[i])

        if i + day[i][0] > n:
            continue

        dp[i + day[i][0]] = max(dp[i + day[i][0]], day[i][1] + dp[i])

    print(max(dp))

if __name__ == '__main__':
    answer = solution()