
check = []
ans = 0

def btr(v,subsum):
    global ans

    if subsum == s :
        ans+=1

    for i in range(v,n):
        btr(i+1,subsum+board[i])

n, s = map(int ,input().split())

board = list(map(int,input().split()))
btr(0,0)

if s == 0:

    ans -=1

print(ans)
