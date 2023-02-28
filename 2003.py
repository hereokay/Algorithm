n, m = map(int, input().split())
board  = list(map(int, input().split()))

left = 0
right = 1
ans = 0

while left <= right and right <= n:

    subBoard = board[left:right]
    total = sum(subBoard)

    if total == m:
        ans += 1
        left += 1
    elif total < m :
        right +=1
    elif total > m:
        left += 1

print(ans)

