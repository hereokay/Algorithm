
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(root):
    stack =[root]
    while stack:
        root = stack.pop()
        for to, dist in graph[root]:
            if visited[to]==-1:
                visited[to] = visited[root]+dist
                stack.append(to)

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    _from, _to, _dist = map(int,input().split())
    graph[_from].append([_to,_dist])
    graph[_to].append([_from,_dist])

visited = [-1]*(n+1)
visited[1]=0
dfs(1)

start = visited.index(max(visited))
visited = [-1]*(n+1)
visited[start] = 0
dfs(start)

print(max(visited))
