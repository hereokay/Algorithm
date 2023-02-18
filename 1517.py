import sys

def recur(start, end ):
    global cnt

    if start < end:
        mid = (start+end) // 2
        recur(start,mid)
        recur(mid+1, end)

        front = start
        back = mid+1
        new_arr = []
        while front <= mid and back <= end :
            if board[front] <= board[back]:
                new_arr.append(board[front])
                front+=1
            else:
                new_arr.append(board[back])
                back+=1
                cnt += mid-front+1
        if front <= mid:
            new_arr = new_arr + board[front : mid+1]
        else:
            new_arr = new_arr + board[back : end+1]

        for i in range(len(new_arr)):
            board[start+i] = new_arr[i]


n = int(input())
board = list(map(int, input().split()))

cnt = 0
recur(0,n-1)

print(cnt)
