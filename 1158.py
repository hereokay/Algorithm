import sys
from collections import deque
input = sys.stdin.readline

n, k = list(map(int,input().split()))

board = deque()
answer = []
for i in range(n):
    board.append(i+1)

idx = 0
while len(board)>0:
    idx += k-1
    idx %= len(board)
    answer.append(str(board[idx]))
    del board[idx]

print("<"+ ", ".join(answer) +">")
