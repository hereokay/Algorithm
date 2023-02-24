n, m = map(int, input().split())

res = []
visited = [0]*(n+1)
# v = 다음 인덱스
# n 끝
def combi(v, cnt):

    if cnt == m:
        print(*res)
        return

    for i in range(v,n+1):
        res.append(i)
        combi(i+1,cnt+1)
        res.pop()


def permu(cnt):
    if cnt==m:
        print(*res)
        return


    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i]=1
            res.append(i)
            permu(cnt+1)
            res.pop()
            visited[i]=0

#permu(0)
combi(1,0)