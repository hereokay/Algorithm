from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x,y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x,y,ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0 <= nx < r) and (0 <= ny < c)) and (board[nx][ny] not in ans):
                    q.add((nx, ny, ans + board[nx][ny]))
                    answer = max(answer, len(ans) + 1)

r, c = map(int, sys.stdin.readline().split())
board =  [list(sys.stdin.readline().strip()) for _ in range(r)]

answer = 1
bfs(0,0)
print(answer)