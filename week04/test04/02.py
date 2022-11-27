# boj. 1520
# time: 37'
# dp problem solving method : top-down

import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph, dp = [], []
answer = 0
for _ in range(m):
    graph.append(list(map(int, input().split())))
    dp.append([-1] * n)

def dfs(x, y):
    if dp[y][x] > -1:
        return dp[y][x]

    cnt = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m: # 그래프 범위 유효성 검사
            if graph[y][x] < graph[ny][nx]:
                # dp 테이블에 채워진 값이 있을 경우 그대로 더함
                cnt += dfs(nx, ny)
            
    dp[y][x] = cnt
    return cnt

dp[0][0] = 1
dfs(n-1, m-1)
print(dp[m-1][n-1])
