from collections import deque

n = int(input())

board = [int(input()) for _ in range(n)]

board.sort(reverse=True)

nega_q = deque()
posi_q = deque()
zero_q = deque()

for i in board:
    if i >0:
        posi_q.append(i)
    if i<0:
        nega_q.append(i)
    if i==0:
        zero_q.append(i)

cnt = 0

while len(posi_q) >= 2:
    a = posi_q.popleft()
    b = posi_q.popleft()
    if a==1 or b==1:
        cnt +=(a+b)
    else:
        cnt += a*b

while len(nega_q) >= 2:
    a = nega_q.pop()
    b = nega_q.pop()
    cnt += a*b

while len(zero_q) >0 and len(nega_q)>0:
    zero_q.popleft()
    nega_q.popleft()

cnt += (sum(posi_q) +sum(nega_q))

print(cnt)
