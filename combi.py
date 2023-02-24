from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

# combinations

res =[]
def btr(v,cnt):

    if cnt == m:
        print(*res)
        return

    for i in range(v,n+1):
        res.append(i)
        btr(i+1,cnt+1)
        res.pop()

btr(1,0)