from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    q = deque([[x,y]])
    board[x][y]=0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]

            if 0 <= nx < 2001 and 0 <= ny <2001:
                if board[nx][ny]==1:
                    board[nx][ny]=0
                    q.append([nx,ny])

n = int(input())

start = []
board = [[0]*2001 for _ in range(2001)]
for i in range(n):
    x1, y1, x2, y2 = map(int,input().split())

    x1+=500 ; x1 *= 2
    x2+=500 ; x2 *= 2
    y1+=500 ; y1 *= 2
    y2+=500 ; y2 *= 2

    start.append([x1,y1])

    for i in range(x1,x2+1):
        board[i][y1]=1
        board[i][y2]=1
    for i in range(y1,y2+1):
        board[x1][i]=1
        board[x2][i]=1

cnt = 0

if board[1000][1000]==1:
    cnt -= 1

for x,y in start:
    if board[x][y]==1:
        cnt+=1
        bfs(x,y)

print(cnt)