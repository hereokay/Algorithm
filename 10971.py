import itertools
import sys

input = sys.stdin.readline

n = int(input())
graph =[list(map(int,input().split())) for _ in range(n)]
ans = sys.maxsize

def dfs(first, current, valueSum, visited=[]):
    global ans

    if valueSum > ans :
        return

    visited = visited + [current]
    if len(visited)==n:
        print(visited)
        if graph[current][first] != 0:
            ans = min(ans, valueSum + graph[current][first])
        return

    for i in range(n):
        if i not in visited:
            if graph[current][i] != 0:
                dfs(first,i,valueSum+graph[current][i],visited)


for i in range(n):
    dfs(i,i,0,[])

print(ans)