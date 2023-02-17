
import sys

sys.setrecursionlimit(10**7)

def dfs(x):
    global ans
    cycle.append(x)
    visited[x]=1
    nextNode = board[x]

    if visited[nextNode]==0:
        dfs(nextNode)
    else:
        if nextNode in cycle:
            ans += cycle[cycle.index(nextNode):]

t = int(input())

for _ in range(t):
    n = int(input())
    board = [0]+list(map(int,input().split()))

    ans = []
    visited = [0]*(n+1)
    for i in range(1,n+1):
        cycle = []
        if visited[i]==0:
            dfs(i)

    print(n - len(ans))

