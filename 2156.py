n = int(input())

board = [int(input()) for _ in range(n)]

dp = [0]*(n+1)


dp[0] = board[0]

if n > 1:
    dp[1] = board[0]+board[1]

if n >2:
    dp[2] = max(
        dp[1],
        board[0]+board[2],
        board[1]+board[2]
    )

for i in range(3,n):
    dp[i] = max(
        dp[i-1],
        dp[i-2] + board[i],
        dp[i-3] + board[i-1] + board[i]
    )

print(dp[n-1])