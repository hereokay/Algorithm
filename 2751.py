import sys

n = int(sys.stdin.readline())

board = [int(sys.stdin.readline()) for _ in range(n)]

board.sort()

for i in range(n):
    sys.stdout.write(str(board[i])+'\n')
