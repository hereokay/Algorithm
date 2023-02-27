

ans = []
def combi(v, cnt):
    if cnt == r:
        print(ans)
        return

    for i in range(v,n):
        ans.append(board[i])
        combi(i+1,cnt+1)
        ans.pop()


def permu(cnt):

    if cnt == r:
        print(ans)
        return

    for i in range(n):
            ans.append(board[i])
            permu(cnt+1)
            ans.pop()



n, r = 5, 2

board =list('ABCDE')
visited = [0]*n
#combi(0,0)
permu(0)