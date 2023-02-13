n = int(input())

board = list(map(int, input().split()))

dp = [0]*(n)

dp[0]= 1

for i in range(1,n):
    for j in range(i):
        if board[j] > board[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))