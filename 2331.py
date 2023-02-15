import sys

a, p = map(int, input().split())
num=0
board =[a]

while True:

    while a>0:
        tmp = a%10
        num += tmp**p
        a /= 10
        a = int(a)

    if num in board:
        break
    else:
        board.append(num)
        a=num
        num=0

print(board.index(num))
