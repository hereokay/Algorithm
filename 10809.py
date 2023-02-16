import sys

input = sys.stdin.readline

word = input().strip()

answer = [-1]*26

for i in range(len(word)):
    if answer[ord(word[i])-ord('a')] == -1:
        answer[ord(word[i])-ord('a')] = i

for i in range(len(answer)):
    print(answer[i],end=' ')
