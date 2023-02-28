import sys

#sys.setrecursionlimit(10**6)

def find(a):
    if parent[a] == a:
        return a
    else:
        p = find(parent[a])
        parent[a] = p
        return p

def union(a,b):
    a = find(a)
    b = find(b)

    if a==b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m =  int(input())

parent = [i for i in range(n+1)]

for a in range(1,n+1):
    tmp = list(map(int ,input().split()))
    for j in range(len(tmp)):
        if tmp[j]==1:
            union(a,j+1)

path = list(map(int, input().split()))

#print(path)
#print(parent)

start = parent[path[0]]
for i in range(m):
    to = path[i]
    if parent[to] != start:
        print('NO')
        break
else:
    print('YES')