import sys
input = sys.stdin.readline

n= int(input())


for i in range(n):
    point = 0
    answer = "YES"
    board = input().strip()
    for j in range(len(board)):
        if board[j] == '(':
            point += 1
        else:
            point -= 1
            if point < 0:
                answer = "NO"

    if point != 0:
        answer = "NO"
    print(answer)
