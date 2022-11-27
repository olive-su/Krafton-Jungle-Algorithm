import sys

input = sys.stdin.readline

n = int(input())
INF = pow(2, 32)
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(0, n-i):
        dp[j][j+i] = INF
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], \
                dp[j][k] \
                + dp[k+1][j+i] \
                + matrix[j][0] * matrix[k][1] * matrix[j+i][1])
            print(dp)

print(dp[0][n-1])

