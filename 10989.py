import sys

input = sys.stdin.readline

n = int(input())

board = [0]*10001

for i in range(n):
    board[int(input())] += 1


for i in range(1, 10001):
    for j in range(board[i]):
        print(i)