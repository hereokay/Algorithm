import sys

input = sys.stdin.readline

while True:

    word = input().rstrip('\n')

    if not word:
        break
    answer = [0]*4

    for i in range(len(word)):
        if word[i] == " ":
            answer[3] += 1
        elif (ord(word[i]) >= ord('0')) and (ord(word[i]) <= ord('9')):
            answer[2] += 1
        elif (ord(word[i]) >= ord('a')) and (ord(word[i]) <= ord('z')):
            answer[0] += 1
        elif (ord(word[i]) >= ord('A')) and (ord(word[i]) <= ord('Z')):
            answer[1] += 1
    print(answer[0], answer[1], answer[2], answer[3])
