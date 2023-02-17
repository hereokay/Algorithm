from collections import deque
import sys

input = sys.stdin.readline



def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        parent = q.popleft()
        for child in graph[parent]:
            if visited[child]==0:
                visited[child]=parent
                q.append(child)

n = int(input())
graph = [[] for _ in range(n+1)]


for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(n+1)
bfs()

for i in range(2,1+n):
    sys.stdout.write(str(visited[i])+"\n")