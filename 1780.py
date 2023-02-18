import sys

n = int(input())

paper =[]
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))


result = {-1:0, 0:0, 1:0}

def divided(row, col, n):
    curr = paper[row][col]

    for i in range(row,row+n):
        for j in range(col,col+n):
            if paper[i][j] != curr:
                next = n //3
                for p in range(3):
                    for q in range(3):
                        divided(row + p * next, col + q * (next), next)
                return
    result[curr] += 1
    return

divided(0,0,n)

for i in result.values():
    print(i)