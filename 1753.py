import heapq
import sys

def bfs(start):
    heapq.heappush(heap,start)
    visited[start] = 0

    while heap:
        parent = heapq.heappop(heap)

        for child, degree in board[parent]:
            next_wei = degree + visited[parent]
            if next_wei < visited[child]:
                visited[child] = next_wei
                heapq.heappush(heap,child)



v, e = map(int ,input().split())
k = int(input())
board = [[] for _ in range(v+1)]
heap = []
visited =[sys.maxsize]*(v+1)

for _ in range(e):
    a, b, c = map(int,input().split())

    board[a].append([b,c])


bfs(k)

print(visited)