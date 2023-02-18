import sys

input = sys.stdin.readline
n, c = map(int ,input().split())

board = []
for i in range(n):
    board.append(int(input()))

board.sort()

# 몇칸을 띄어서 설치하느지가 중아ㅛ한거나잖아
mini = 1
maxi = board[-1] - board[0]
mid = 0
while mini <= maxi:
    mid = (mini+maxi)//2
    cur = board[0]
    count = 1
    for i in range(1,len(board)):
        if board[i] >= cur + mid:
            count +=1
            cur = board[i]

    if count >= c: # mid 가 작았다
        mini = mid+1
    else:
        maxi = mid-1


print(maxi)
