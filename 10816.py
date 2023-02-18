
n = int(input())
tmp = list(map(int, input().split()))
tmp.sort()

dict_board = {}
for i in range(n):
    if tmp[i] not in dict_board:
        dict_board[tmp[i]] =1
    else:
        dict_board[tmp[i]] = dict_board[tmp[i]] +1

list_board = list(dict_board.items())
list_board.sort()

m = int(input())
targets = list(map(int, input().split()))

idx =[0]*(m)

for i in range(len(targets)):
    target = targets[i]
    start = 0
    end = len(list_board)-1
    while start <= end:
        mid = (start+end) // 2

        value_mid, num_mid = list_board[mid]

        if value_mid == target:
            idx[i]= num_mid
            break
        elif value_mid < target:
            start = mid+1
        else:
            end = mid-1

print(" ".join(str(s) for s in idx))


