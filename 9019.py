import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q =deque()
    q.append(start)
    visited[start]= 1

    while q:
        v = q.popleft()
        sv = str(v)
        while len(sv)< 4:
            sv = "0"+sv
        if v == end:
            return

        candidnate =[
            (v*2)%10000,
            (v-1)%10000,
            int(sv[1:4]+sv[0])%10000,
            int(sv[3]+sv[:3])%10000
        ]

        print(v)
        print(candidnate)
        dd = ["D","S","L","R"]
        for i in range(len(candidnate)):
            target = candidnate[i]
            if visited[target]==0:
                q.append(target)
                cmd[target] = cmd[v]+dd[i]
                visited[target]=1


t = int(input())
for _ in range(t):
    start, end = map(int, input().split())
    cmd = ["" for _ in range(10 ** 4 + 1)]
    visited = [0]*(10**4+1)
    bfs()
    print(cmd[end])