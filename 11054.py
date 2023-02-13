n = int(input())

board = list(map(int, input().split()))

dp_inc = [0]*(n)
dp_dec = [0]*(n)

dp_inc[0] = 1
dp_dec[0] = 1


for i in range(1,n):
    for j in range(i):
        if board[j] < board[i] and dp_inc[j] > dp_inc[i]:
            dp_inc[i]=dp_inc[j]
    dp_inc[i] += 1

board.reverse()

for i in range(1,n):
    for j in range(i):
        if board[j] < board[i] and dp_dec[j] > dp_dec[i]:
            dp_dec[i]=dp_dec[j]
    dp_dec[i] +=1

dp_dec.reverse()

answer = [dp_inc[i]+dp_dec[i] for i in range(n)]


print(max(answer)-1)
