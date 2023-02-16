import sys

input = sys.stdin.readline

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a, a)

n = int(input())

for i in range(n):
    a,b = list(map(int, input().split()))

    g_ab = gcd(a,b)
    print(int((a*b)/g_ab))


