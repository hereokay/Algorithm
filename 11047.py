n, k = map(int, input().split())

board = [int(input()) for _ in range(n)]

board.sort(reverse=True)

ans = 0
for i in range(n):

    q = k // board[i]
    k -= q*board[i]
    ans += q
    if k==0:
        break


print(ans)
