import sys


def backT(cnt,idx):

    if cnt == l :
        co,vo = 0,0
        for i in range(l):
            if ans[i] in ['a','e','i','o','u']:
                co +=1
            else:
                vo+=1
        if co >=1 and vo >= 2:
            print("".join(ans))
        return

    for i in range(idx,c):
        ans.append(board[i])
        backT(cnt+1,i+1)
        ans.pop()




l, c = map(int,input().split())
board = list(input().split())
board.sort()
ans = []
print(board)
backT(0,0)
