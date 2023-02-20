
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def dfs(x,y,idx):# idx가 다음걸 가리키는 구나 ㅎ

    if visited[x][y][idx] != -1:
        return visited[x][y][idx]

    #print(x+1,y+1,idx)
    if len(word)-1 == idx:
        return 1

    visited[x][y][idx] = 0
    for i in range(4):
        for plus in range(1,k+1):
            if plus == 0:
                continue
            nx = x +dx[i]*plus
            ny = y +dy[i]*plus
            if 0<= nx < n and 0<= ny < m:
                if board[nx][ny]==word[idx+1]:
                    visited[x][y][idx] += dfs(nx,ny,idx+1)
    return visited[x][y][idx]



n,m,k = map(int, input().split())

board = [list(input()) for _ in range(n)]
word = input().strip()
visited = [[[-1]*(len(word)) for _ in range(m+1)] for _ in range(n+1)]

ans = 0
for i in range(n):
    for j in range(m):
        if word[0]==board[i][j]:
            ans += dfs(i,j,0)

print(ans)
