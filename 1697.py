import sys
from collections import deque
input = sys.stdin.readline

ans = 0
def bfs():
    global ans # min

    q = deque()
    q.append(current)
    visited[current] = 0
    while q:
        child = q.popleft()
        #print(child,end=' ')
        if child == distination:
            #print()
            print(visited[child])
            exit()
        candidate = [child+1, child-1, child*2]
        for can in candidate:
            if 0 <= can <= 200000+1:
                if visited[can] == -1:
                    q.append(can)
                    visited[can] = visited[child] + 1


current, distination = map(int,input().split())
visited = [-1]*(2000000 + 1) # 범위가 최대 n의 2배

bfs()