import sys

input = sys.stdin.readline

n = int(input())

board = list(map(int, input().split()))
board.sort()
m = int(input())
check = list(map(int, input().split()))

idx = [0]*(m)
for i in range(len(check)):
    start = 0
    end = len(board)-1

    exist = False
    while start <= end:
        mid = (start+end) // 2

        if board[mid] > check[i]:
            end = mid - 1
        elif board[mid] < check[i]:
            start = mid + 1
        else:
            idx[i]=1
            break


print(" ".join(str(s) for s in idx))