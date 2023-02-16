import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
myDeque = deque()

for i in range(n):
    cmd = input().strip()

    if cmd[0:4] == "push":
        cmd, num = cmd.split()
        num = int(num)
        myDeque.append(num)
    if cmd[0:3] == 'pop':
        if len(myDeque) >0:
            print(myDeque.popleft())
        else:
            print(-1)
    if cmd[0:5]=='size':
        print(len(myDeque))
    if cmd[0:5]=='empty':
        if len(myDeque) >0:
            print(0)
        else:
            print(1)
    if cmd[0:5] == 'front':
        if len(myDeque) >0:
            print(myDeque[0])
        else:
            print(-1)
    if cmd[0:4] == 'back':
        if len(myDeque) > 0:
            print(myDeque[-1])
        else:
            print(-1)
