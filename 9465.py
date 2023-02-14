t = int(input())

for _ in range(t):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(3)]

    dp[0][0] = 0
    dp[1][0] = board[0][0]
    dp[2][0] = board[1][0]

    for i in range(1,n):
        dp[0][i] = max([dp[0][i-1],dp[1][i-1],dp[2][i-1]])
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + board[0][i]
        dp[2][i] = max(dp[0][i-1],dp[1][i-1]) + board[1][i]

    print(max([dp[0][n-1],dp[1][n-1],dp[2][n-1]]))