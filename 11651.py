import sys
input = sys.stdin.readline

n = int(input())

board = [[0]*2 for _ in range(n)]

for i in range(n):
    board[i][1], board[i][0] = list(map(int, input().split()))

board.sort()

for i in range(n):
    print(str(board[i][1]) + " "+ str(board[i][0]))

