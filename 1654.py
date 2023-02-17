k, n = map(int,input().split())

board = []
for _ in range(k):
    board.append(int(input()))

start = 1
end = max(board)

while start<= end:
    lines = 0
    mid =( start+end)//2
    for i in range(k):
        lines += board[i] // mid

    # mid가 너무작아서 라인이 많은경우 -> mid 증가시켜
    if lines >= n :
        start = mid+1
    else:
        end = mid-1

print()
