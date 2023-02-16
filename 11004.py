import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))

board = list(map(int, input().split()))

board.sort()

print(board[k-1])