import sys
from collections import deque

input = sys.stdin.readline


def bfs1(i, j, g):
    q = deque()
    vis[i][j] = True
    q.append([i, j])
    board[i][j] = g

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < n and 0 <= nj < n:
                if board[ni][nj] == 1 and vis[ni][nj] == 0:
                    vis[ni][nj] = 1

                    board[ni][nj] = g
                    q.append([ni, nj])


# z인 땅에 대해서 주변 거리저장
def bfs2(z):
    global ans
    dist = [[0] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == z:
                q.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 0 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
                if board[nx][ny] > 0 and board[nx][ny] != z:
                    ans = min(ans, dist[x][y])
                    return


# 색을 칠하고 거리를 제야겠다.

n = int(input())

board = [[0] * (n) for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
g = 2
vis = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not vis[i][j]:
            bfs1(i, j, g)
            g += 1
ans = sys.maxsize
for i in range(2, g + 1):
    bfs2(i)

print(ans)