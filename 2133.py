n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = 1

for i in range(n+1):
    for j in range(2,k+1):
        dp[i][j] = sum([dp[a][j-1] for a in range(i+1)])

print(dp[n][k] % 10**9)
