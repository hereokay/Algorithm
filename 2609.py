import sys

input = sys.stdin.readline

def gcd(a, b):
    if a==0:
        return b
    return gcd(b%a , a)

a, b = list(map(int, input().split()))

answer1 = gcd(a, b)
answer2 =int( (a/answer1) * (b))

print(answer1)
print(answer2)
