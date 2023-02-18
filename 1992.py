import sys
input = sys.stdin.readline

def recur(row,col,n):
    first = board[row][col]


    for i in range(n):
        for j in range(n):
            if board[row+i][col+j] != first:
                ans.append("(")
                l = n //2
                for p in range(2):
                    for q in range(2):
                        recur(row+l*p,col+l*q,l)
                ans.append(")")
                return

    ans.append(str(first))


n = int(input())

board = [[0]*n for _ in range(n)]
for i in range(n):
   tmp = input()
   for j in range(n):
       board[i][j]=tmp[j]
ans = []
recur(0,0,n)

print("".join(ans))