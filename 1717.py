import sys

sys.setrecursionlimit(10**7)
def find(a):
    if parent[a] == a:
        return a
    else:
        p = find(parent[a])
        parent[a] = p
        return p

def union(a, b):
   a = find(a)
   b = find(b)

   if a==b:
       return
   else:
       parent[b] = a


n, m = map(int,input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i]=i

for _ in range(m):
    o,a,b = map(int, input().split())

    if o==0: # 합연산
        union(a,b)
    else: # 서치연산
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
