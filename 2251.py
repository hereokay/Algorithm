from collections import deque

q = deque()
def bfs():
    q.append([0,0,cap_abc[2]])

    visited[0][0]=cap_abc[2]

    while q:
        l_abc = q.popleft()

        for _from in range(3):
            for _to in range(3):
                if _from == _to:
                    continue
                if l_abc[_from] > 0 and l_abc[_to] != cap_abc[_to]:
                    test_abc = l_abc.copy()
                    trans(test_abc,_from,_to)


def trans(l_abc, _from, _to):
    water = min(l_abc[_from],cap_abc[_to]-l_abc[_to])
    l_abc[_from] -=water
    l_abc[_to] += water
    if visited[l_abc[0]][l_abc[1]] == -1:
        visited[l_abc[0]][l_abc[1]] =l_abc[2]
        q.append(l_abc)



cap_abc = list(map(int,input().split()))


visited = [[-1]*201 for _ in range(201)]

bfs()

ans = []
for j in range(0,1+cap_abc[1]):
    if visited[0][j] != -1:
        #print(str(0),str(j),visited[0][j])
        ans.append(visited[0][j])

ans.sort()
print(*ans)
