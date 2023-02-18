import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A_arr = list(map(int,input().split()))
B_arr = list(map(int, input().split()))

sumAB = A_arr+B_arr
sumAB.sort()
print(*sumAB)
