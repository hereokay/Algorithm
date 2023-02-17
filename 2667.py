from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    q = deque()
    cnt = 0
    q.append([i,j])
    board[i][j]=0
    while q:
        cur = q.popleft()
        cnt += 1
        for idx_d in range(4):
            near_x = cur[0]+dx[idx_d]
            near_y = cur[1]+dy[idx_d]

            if board[near_x][near_y]==1:
                board[near_x][near_y]=0
                q.append([near_x,near_y])
    return cnt


n = int(input())

board = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, 1+n):
    str = input()
    for j in range(1,n+1):
        board[i][j]=int(str[j-1])

ans = []

for i in range(1,n+1):
    for j in range(1,n+1):
        if board[i][j]==1:
            ans.append(bfs(i,j))

ans.sort()
l = len(ans)
print(l)
for i in range(l):
    print(ans[i])