from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            if 0 < nx < h+1 and 0 < ny < w+1 :
                if board[nx][ny]==0:
                    board[nx][ny]=board[x][y]+1
                    q.append([nx,ny])


w, h = map(int,input().split())

board = [[0]*(w+2) for _ in range(h+2)]

for i in range(1,h+1):
    board[i] = [0] + list(map(int,input().split())) + [0]

q =deque()
for i in range(1,h+1):
    for j in range(1,w+1):
        if board[i][j] == 1:
            q.append([i,j])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

bfs()

ans = 0
for i in range(1,h+1):
    for j in range(1, w+1):
        if board[i][j]==0:
            print(-1)
            exit()
        else:
            ans = max(ans,board[i][j])

print(ans-1)