n = int(input())

board = list(map(int,input().split()))

board.sort()

ans = 0
for i in range(len(board)):
    ans += board[i]*(len(board)-i)

print(ans)