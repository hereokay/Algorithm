n = int(input())

board = list(map(int, input().split()))
board = [0] + board

dp = [0]*(n+1)
dp[1] = board[1]


for i in range(1,n+1):
    for j in range(i+1):
        if dp[i] < dp[i-j]+board[j]:
            dp[i] = dp[i-j]+board[j]

print(dp[n])
