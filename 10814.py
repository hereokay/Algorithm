import sys
input = sys.stdin.readline

n = int(input())

board = [[0]*2 for _ in range(n)]

for i in range(n):
    board[i] = list(input().split())
    board[i][0] = int(board[i][0])

board.sort(key= lambda x : x[0])

for i in range(n):
    print(str(board[i][0])+" "+board[i][1])