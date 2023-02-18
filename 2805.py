n, m = map(int, input().split())

board= list(map(int, input().split()))

start, end = 1, max(board)

while start<=end:
    total = 0
    mid = (start+end)// 2

    for i in board:
        tmp = i - mid
        if tmp>0:
            total += tmp

    if total >= m: # 증가
        start = mid+1
    else:
        end = mid-1

print(end)