n, m = map(int, input().split())
board = list(map(int, input().split()))
board = board + [0]
left, right = 0, 0
answer = float("inf")
sumValue = board[0]
while right < n:
    if sumValue < m:
        right += 1
        sumValue += board[right]

    elif sumValue >= m:
        answer = min(answer, right - left + 1)
        sumValue -= board[left]
        left += 1

if answer == float("inf"):
    print(0)
else:
    print(answer)
