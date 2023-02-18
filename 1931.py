import sys
input = sys.stdin.readline

n = int(input())

board = [[0,0] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

board.sort(key= lambda x : (x[1],x[0]))

current = 0
cnt = 0
for i in range(len(board)):
    s, e = board[i]
    if current <=s:
        current=e
        cnt += 1

print(cnt)