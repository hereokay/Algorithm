
n = int(input())

for _ in range(n):
    str = input()

    cnt=0
    ans =0
    for i in range(len(str)):
        if str[i]=='O':
            cnt+=1
            ans+=cnt
        else:
            cnt=0

    print(ans)