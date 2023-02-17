from collections import deque

def bfs():
    x=y=1

    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if board[nx][ny] == 1 :
                board[nx][ny] = board[x][y]+1
                q.append([nx, ny])
                if board[h][w] != 1:
                    return

h, w = map(int, input().split())

board = [[0]*(w+2) for _ in range(h+2)]

for i in range(1,1+h):
    str = input()
    for j in range(len(str)):
        board[i][j+1] = int(str[j])

dx = [0,1,0,-1]
dy = [1,0,-1,0]
bfs()

print(board[h][w])
