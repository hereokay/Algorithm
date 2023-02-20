import itertools

n = int(input())
board = list(map(int, input().split()))

nPr = itertools.permutations(board,len(board))

ans = 0
for tu in nPr:
    tmp = 0
    for i in range(len(tu)-1):
        tmp += abs(tu[i+1]-tu[i])
    ans = max(ans,tmp)



print(ans)