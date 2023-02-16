import sys

input = sys.stdin.readline

line = input()[:-1]

answer = []
for i in range(len(line)):
    answer.append(line[i:])

answer.sort()

print(" ".join(answer))