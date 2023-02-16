import sys

input = sys.stdin.readline

line = input()[:-1]
answer = ""
for i in range(len(line)):

    if (line[i] >= 'a') and (line[i] <= 'z'):
        idx = ord(line[i]) - ord('a') + 13
        idx %= 26
        idx += ord('a')
        answer += chr(idx)
    elif (line[i]>='A') and (line[i] <= 'Z'):
        idx = ord(line[i]) - ord('A') + 13
        idx %= 26
        idx += ord('A')
        answer += chr(idx)
    else:
        answer += line[i]

print(answer)
