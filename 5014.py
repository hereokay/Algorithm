from collections import deque

def bfs():
    q = deque()
    q.append(current)
    visited[current]=1

    while q:
        parent = q.popleft()

        if parent==target:
            break

        d_parent = parent- down
        if 1 <= d_parent :
            if visited[d_parent]==0:
                visited[d_parent]=visited[parent]+1
                q.append(d_parent)
        u_parent = parent + up
        if u_parent <= end:
            if visited[u_parent]==0:
                visited[u_parent] = visited[parent]+1
                q.append(u_parent)


end, current, target, up, down = map(int,input().split())


visited = [0]*(10**6+1)

bfs()

if visited[target]!=0:
    print(visited[target]-1)
else:
    print("use the stairs")