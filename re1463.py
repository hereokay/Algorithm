from collections import deque


def sol(start):

    q = deque()
    q.append((start,1))
    dp[start]=1

    while q:
        next_node, degree = q.popleft()
        #print(next_node, degree)
        if next_node == 1:
            return degree

        if next_node % 2==0 and dp[next_node//2]==0:
            dp[next_node // 2]=1
            q.append((next_node//2, degree+1))
        if next_node %3 ==0 and dp[next_node//3]==0:
            dp[next_node // 3]=1
            q.append((next_node // 3, degree+1))
        if dp[next_node-1]==0:
            dp[next_node-1] = 1
            q.append((next_node-1, degree+1))

x = int(input())
dp = [0]*(x+1)

tmp = sol(x)
print(tmp-1)