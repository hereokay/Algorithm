import sys
from collections import deque


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    while q:
        now = q.popleft()

        if now == "123456780":
            return cntDict[now]

        zero_pos = now.find("0")
        x = zero_pos // 3
        y = zero_pos % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                nPos = nx * 3 + ny
                list_now = list(now)
                list_now[nPos], list_now[zero_pos] = list_now[zero_pos], list_now[nPos]
                list_now = "".join(list_now)

                if not cntDict.get(list_now):
                    q.append(next())





start =""
for _ in range(3):
    temp = sys.stdin.readline().strip()
    start += temp.replace(" ","")

q = deque()
q.append(start)

cntDict = dict()
cntDict[start]= 0

result = bfs()
try:
    print(result)
except:
    print(-1)