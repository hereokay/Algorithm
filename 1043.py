n, m = map(int ,input().split())
knowList = set(map(int, input().split()[1:]))
#knowList = set(input().split()[1:])
board = []

for _ in range(m):
    board.append(set(map(int, input().split()[1:])))

for _ in range(m):
    for party in board:
        if party & knowList:
            knowList = knowList.union(party)

cnt =0
for party in board:
    if party & knowList:
        continue
    cnt += 1

print(cnt)

