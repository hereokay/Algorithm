from collections import deque

n,m = map(int ,input().split())
graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b]+=1

q = deque()
for i in range(1,1+n):
    if degree[i]==0:
        q.append(i)

answer = []
while q:
    tmp = q.popleft()
    answer.append(tmp)

    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i]==0:
            q.append(i)

print(*answer)