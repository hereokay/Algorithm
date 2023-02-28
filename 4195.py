import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x not in parent:
        parent[x] = x

    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a== b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


t = int(input())
for _ in range(t):
    n = int(input())

    parent = dict()

    for i in range(n):
        name1, name2 = list(input().split())
        union(name1,name2)

        target = parent[name1]
        cnt = 0
        ans = []
        for name in parent:
            if find(name) == target:
                cnt +=1
                ans.append(name)
        print(cnt)
        #print(ans)
        #print(parent)