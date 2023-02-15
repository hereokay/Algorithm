import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

def bfs(v):
    q = deque()
    q.append(v)
    visited[v]=1

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)


for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)

    line = list(map(int,input().split()))
    for i in range(n):
        a = i+1
        b = line[i]
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for i in range(1,n+1):
        if visited[i]==0:
            bfs(i)
            cnt +=1

    print(cnt)


