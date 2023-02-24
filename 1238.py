import heapq
import sys

input = sys.stdin.readline


def di(start,end):
    heap = []
    visited = [sys.maxsize] * (n + 1)

    heapq.heappush(heap,(0, start))
    visited[start]=0

    while heap:
        dist, parent = heapq.heappop(heap)

        for node_index, node_cost in graph[parent]:
            cost = dist + node_cost

            if visited[node_index] > cost:
                visited[node_index] = cost
                heapq.heappush(heap, (cost, node_index))

    return visited[end]

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append([b,cost])

distance = 0
for i in range(1,n+1):
    go = di(i,x)
    back =di(x,i)
    distance = max(distance, go+back)

print(distance)