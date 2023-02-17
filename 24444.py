import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    idx = 1
    visited[start] = idx
    idx +=1
    q = deque([start])

    while q:
        v = q.popleft()
        for i in (graph[v]):
            if visited[i]==0:
                visited[i]=idx
                idx+=1
                q.append(i)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n + 1)]
count =1
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    graph[i].sort()

bfs(r)

for i in range(1,n+1):
    print(visited[i])