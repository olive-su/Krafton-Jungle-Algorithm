import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(i, -1, -1):
        if arr[j] < arr[i] and dp[j] > dp[i]: # 현재 원소 보다 작음
            dp[i] = dp[j]
    dp[i] += 1 # 현재 원소 추가

print(max(dp))
