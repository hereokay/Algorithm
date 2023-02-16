import sys

input = sys.stdin.readline

n = int(input())

board = []

for i in range(n):
    cmd = input()
    if cmd[0:4] == "push":
        cmd, num = cmd.split()
        num = int(num)
        board.append(num)

    if cmd[0:3] == "pop":
        if len(board)>0:
            print(board.pop())
        else:
            print(-1)

    if cmd[0:3] == "top":
        if len(board) > 0:
            print(board[-1])
        else:
            print(-1)

    if cmd[0:4] == "size":
        print(len(board))

    if cmd[0:5] == "empty":
        if len(board) == 0:
            print(1)
        else:
            print(0)

