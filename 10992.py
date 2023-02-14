n = int(input())

for i in range(1,n+1):
    for j in range(1,2*n):
        if (( j == (i+n-1)) or ( (i+j) == n+1 )) and (((i+j)%2)!=(n%2)):
            print('*', end='')
        elif i==n:
            print('*', end='')
        elif (j <= (i+n-1)):
            print(' ', end='')
    if i != n:
        print()