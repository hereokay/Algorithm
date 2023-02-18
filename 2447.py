import sys

def recur(row,col,n):
    if n==1:
        board[row][col]='*'
        return

    l = n//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                empty(row+l*i,col+l*j,l)
            else:
                recur(row+l*i,col+l*j,l)

def empty(row,col ,n):
    for i in range(n):
        for j in range(n):
            board[row+i][col+j] =' '

n = int(input())

board= [[0]*n for _ in range(n)]
recur(0,0,n)

for i in range(n):
    sys.stdout.write("".join(board[i]) + "\n")