import sys
input = sys.stdin.readline

line = input()[:-1]

n = int(input())

left_list = list(line)
right_list = []

for i in range(n):
    cmd = input()[:-1]

    if cmd=="L":
        if len(left_list) >0:
            tmp = left_list.pop()
            right_list.append(tmp)
    elif cmd=="D":
        if len(right_list) >0:
            tmp = right_list.pop()
            left_list.append(tmp)
    elif cmd=="B":
        if len(left_list) > 0:
            left_list.pop()
    elif cmd[0] =="P":
        cmd, tmp = cmd.split()
        left_list.append(tmp)


right_list.reverse()

print("".join(left_list)+"".join(right_list))