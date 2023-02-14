import sys
input = sys.stdin.readline


n = int(input())

board = [[0]*3 for _ in range(n)]

for i in range(n):
    board[i] = list(input().split())
    board[i][1:4] = list(map(int, board[i][1:4]))


board.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))


for i in range(n):
    print(board[i][0])
