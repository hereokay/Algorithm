import sys

input = sys.stdin.readline

n = int(input())

board = {}

for i in range(n):
    tmp = int(input())
    if tmp in board:
        board[tmp] = board[tmp]+1
    else:
        board[tmp] = 1


l = list(board.items())
l.sort(key= lambda x: (-x[1], x[0]))


print(l[0][0])
