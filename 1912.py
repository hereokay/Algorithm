n = int(input())

board = list(map(int, input().split()))

dp = [0]*(n)
dp[0]=board[0]

for i in range(1,n):
    dp[i] = max(dp[i-1], 0) + board[i]

print(max(dp))
