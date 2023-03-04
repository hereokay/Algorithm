
n =5
m= 3
ans =[]
def combi(v, cnt):
    if cnt==m:
        print(*ans)
        return

    for i in range(v,n):
        ans.append(i)
        combi(i+1,cnt+1)
        ans.pop()

visited = [0]*(n)
def permu(cnt):

    if cnt==m:
        print(*ans)
        return

    for i in range(n):
        if visited[i] ==0:
            ans.append(i)
            visited[i]=1
            permu(cnt+1)
            ans.pop()
            visited[i]=0




permu(0)