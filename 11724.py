import sys
from collections import deque

input = sys.stdin.readline


def dfs(v):
    stack = [v]
    visited.append(v)
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if i not in visited:
                stack.append(i)
                visited.append(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

total = [i for i in range(1,n+1)]
cnt =0
while True:

    rest = list(set(total)-set(visited))
    if len(rest)==0:
        break
    dfs(rest[0])
    cnt += 1
print(cnt)

