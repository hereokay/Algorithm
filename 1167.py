# 가장 먼곳을 dfs로 찾아야 한다.
import sys

input = sys.stdin.readline


def dfs1(parent):
    for e,d in graph[parent]:
        if visited[e]==-1:
            visited[e]= visited[parent]+d
            dfs1(e)

def dfs2(z):

    pass


n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(1,1+n):
    line = list(map(int, input().split()))

    length = len(line)
    for i in range(1, length//2):
        graph[line[0]].append([line[2*i-1],line[2*i]])

visited= [-1]*(n+1)
visited[1] = 0
dfs1(1)

start = visited.index(max(visited))

visited= [-1]*(n+1)
visited[start]=0
dfs1(start)

print(max(visited))