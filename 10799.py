import sys
input = sys.stdin.readline

str = input()

str = str.replace('()',"*")

stack = []
answer = 0
for i in range(len(str)):
    if str[i] =='*':
        answer += len(stack)
    elif str[i]=='(':
        stack.append(1)
    elif str[i]==')':
        stack.pop()
        answer += 1

print(answer)
