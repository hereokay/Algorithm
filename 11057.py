n = int(input())

dp = [[0]*11 for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2,n+1):
    dp[i][0] = dp[i - 1][0]

    for j in range(1,10):
        dp[i][j] = sum(dp[i-1][:j+1])

print(sum(dp[n]) % 10007)
