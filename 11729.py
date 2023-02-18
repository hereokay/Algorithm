
def hanoi(_from, _by,_to, _count):
    if _count==0:
        return

    hanoi(_from,_to,_by,_count-1)
    trans(_from,_to)
    hanoi(_by,_from,_to,_count-1)


def trans(_from, _to):
    ans.append([_from+1,_to+1])
    tmp = stack[_from].pop()
    stack[_to].append(tmp)

n = int(input())
stack = [[] for _ in range(3)]
ans = []
for i in range(n):
    stack[0].append(n-i)

hanoi(0,1,2,n)

print(len(ans))
for info in ans:
    print(*info)