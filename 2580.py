from collections import deque
import sys

input = sys.stdin.readline

tmp = set([1,2,3,4,5,6,7,8,9])
def backT(idx):

    if idx == len(blank):
        for i in range(9):
            print(*board[i])
        exit()
    x, y = blank[idx]
    bound_x = (x - x%3)
    bound_y = (y - y%3)
    sum1 = set()
    for i in range(bound_x,bound_x+3):
        for j in range(bound_y,bound_y+3):
            sum1.add(board[i][j])
    for i in range(9):
        sum1.add(board[i][y])
        sum1.add(board[x][i])

    candidnate = tmp - sum1
    for num in candidnate:
        board[x][y]=num
        backT(idx+1)
        board[x][y]=0


board = [list(map(int,input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            blank.append([i,j])

backT(0)
