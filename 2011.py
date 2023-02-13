numbers = list(map(int, list(input())))
n = len(numbers)
dp = [0]*(n+1)

dp[0] = 1
if numbers[0] == 0:
    print(0)
    exit()

if n > 1:
    if numbers[1] > 0:
        dp[1] = dp[0]

    tmp = numbers[0]*10 + numbers[1]
    if (tmp > 0) and (tmp <= 26):
        dp[1] += 1

# 2, 3, 4, ... n-1
for i in range(2, n):
    if (numbers[i] > 0) and (numbers[i] <= 26):
        dp[i] = (dp[i-1] % 10**6)

    tmp = numbers[i-1]*10 + numbers[i]
    if (tmp <= 26) and (tmp >= 10):
        dp[i] += (dp[i-2] % 10**6)


print(dp[n-1] % 10**6)
