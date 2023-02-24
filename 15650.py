n, m = map(int ,input().split())

res = []
# 지금들어올대 가리키는 v
# 지금 갯수
def combi(v, cnt):
    if cnt ==m :
        print(*res)
        return

    for i in range(v,n+1):
        res.append(i)
        combi(i+1,cnt+1)
        res.pop()


combi(1,0)