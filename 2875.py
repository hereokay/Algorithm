

n,m,k = map(int,input().split())

# n = 11, m= 5 , k =3

# 팀을 먼저 만들어
team = min(n//2,m)

# 팀원수만큼 빼기
n -= team*2
m -= team

# 남은 사람 인턴쉽
if n > 0:
    k -= n
if m > 0:
    k -= m

if k >0:
    # k =10이면 k//3 = 3
    sub = k//3

    team -= sub
    k -= sub*3
    if k > 0:
        team -=1



if team < 0:
    print(0)
else:
    print(team)






