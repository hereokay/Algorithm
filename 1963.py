import sys
from collections import deque

def setPrime():
    for i in range(2,101):
        if prime[i]:
            for j in range(i*2,10**4+1,i):
                prime[j] = 0

def bfs():
    q = deque()
    q.append(start)


    visited[start] = 1
    while q:
        v = q.popleft()

        if v== end:
            return True
        str_v = str(v)
        for i in range(4):
            for j in range(10):
                can = int(str_v[:i] + str(j) + str_v[i+1:])

                if prime[can] and visited[can] ==0 and can >= 1000:
                    visited[can] =visited[v]+1
                    q.append(can)
    return False


t = int(input())

prime = [1]*(10**4 + 1)
setPrime()

for _ in range(t):
    start, end = map(int,input().split())
    visited = [0] * (10 ** 4 + 1)

    if bfs():
        print(visited[end]-1)
    else:
        print("Impossible")






