# boj. 1890
# time : 11'
# dp problem solving method : bottom-up

import sys

input = sys.stdin.readline
n = int(input())
graph = []
dp = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    dp.append([0] * n)

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break
        ni = i + graph[i][j]
        nj = j + graph[i][j]
        if ni < n:
            dp[ni][j] += dp[i][j]
        if nj < n:
            dp[i][nj] += dp[i][j]

print(dp[n-1][n-1])