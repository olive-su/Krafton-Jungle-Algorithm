import sys

input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
w, v = [0] * (n + 1), [0] * (n + 1)

for i in range(1, n + 1):
    a, b = map(int, input().split())
    w[i], v[i] = a, b

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else: dp[i][j] = dp[i - 1][j]

print(dp[n][k])
