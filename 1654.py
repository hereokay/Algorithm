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
    if lines > n :
        start = mid+1
    elif lines < n :
        end = mid-1 # 200~ 201 개 중 최대값
    else:
        pass
# 같을때 증가시켜주면 최대쪽으로 가게되고
# 같을때 감소시켜주면 최소쪽으로 가게되고
# 최대가 결정됬을떈 증가되서 end가 정상범위에 속할때 종료되고
# 최소가 결정됬을땐 감소되서 start가 정상범위에 속할때 종료된다.

print(start)

#https://lotuslee.tistory.com/60