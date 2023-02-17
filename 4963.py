from collections import deque

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,1,-1]

def bfs(x,y):
    q = deque()
    board[x][y]=0
    q.append([x,y])

    while q:
        cur = q.popleft()

        for i in range(8):
            next_x = cur[0] + dx[i]
            next_y = cur[1] + dy[i]
            if board[next_x][next_y]==1:
                board[next_x][next_y]=0
                q.append([next_x,next_y])



while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break

    board = [[0]*(w+2) for _ in range(h+2)]
    for i in range(1,1+h):
        board[i] = [0] + list(map(int,input().split())) + [0]

    ans = 0
    for i in range(1,h+1):
        for j in range(1,w+1):
            if board[i][j]==1:
                bfs(i,j)
                ans+=1
    print(ans)