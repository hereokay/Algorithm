n,m = map(int,input().split())

rectangle_input = [[0]*(m) for _ in range(n)]

for i in range(n):
    line_input = list(map(int,list(input())))
    rectangle_input[i] = (line_input)

ans =0

def getsum(x1,y1,x2,y2):
    ret = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
           ret += rectangle_input[i][j]
    return ret



# case 1
# 123
# 123
# 123
for i in range(0,m-2): # 0 ~ m-2
    for j in range(i+1,m-1): # i+1 ~ m-1
        sum1 = getsum(0,0,n-1,i)
        sum2 = getsum(0,i+1,n-1,j)
        sum3 = getsum(0,j+1,n-1,m-1)
        ans = max(ans, sum1*sum2*sum3)

# case 2
# 111
# 222
# 333
for i in range(0,n-2):
    for j in range(i+1,n-1):
        sum1 = getsum(0,0,i,m-1)
        sum2 = getsum(i+1,0,j,m-1)
        sum3 = getsum(j+1,0,n-1,m-1)
        ans = max(ans, sum1 * sum2 * sum3)
# case 3
# 1 2 2
# 1 3 3
# 1 3 3
for i in range(0,m-1):
    for j in range(0,n-1):
        sum1 = getsum(0,0,n-1,i)
        sum2 = getsum(0,i+1,j,m-1)
        sum3 = getsum(j+1,i+1,n-1,m-1)
        ans = max(ans, sum1 * sum2 * sum3)

# case 4
# 1 3 3
# 2 3 3
# 2 3 3
for i in range(0,m-1):
    for j in range(0,n-1):
        sum1 = getsum(0,0,j,i)
        sum2 = getsum(j+1,0,n-1,i)
        sum3 = getsum(0,i+1,n-1,m-1)
        ans = max(ans, sum1 * sum2 * sum3)

# case 5
# 1 2 2
# 1 2 2
# 3 3 3
for i in range(0,m-1):
    for j in range(0,n-1):
        sum1 = getsum(0,0,j,i)
        sum2 = getsum(0,i+1,j,m-1)
        sum3 = getsum(j+1,0,n-1,m-1)
        ans = max(ans, sum1 * sum2 * sum3)

# case 6
# 1 1 1
# 1 1 1
# 2 3 3
for i in range(0,m-1):
    for j in range(0,n-1):
        sum1 = getsum(0,0,j,m-1)
        sum2 = getsum(j+1,0,n-1,i)
        sum3 = getsum(j+1,i+1,n-1,m-1)
        ans = max(ans, sum1 * sum2 * sum3)


print(ans)