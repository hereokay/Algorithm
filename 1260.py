import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited2.append(v)

    while q:
        v = q.popleft()
        print(v,end=' ')
        for n in graph[v]:
            if n not in visited2:
                q.append(n)
                visited2.append(n)



def dfs(v):
    print(v,end =' ')
    visited.append(v)
    for n in graph[v]:
        if n not in visited:
            dfs(n)





n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = []
visited2 =[]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print()
bfs(v)