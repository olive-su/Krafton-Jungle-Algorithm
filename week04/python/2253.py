import sys

input = sys.stdin.readline
n, m = map(int, input().split())
LIMIT = int((2 * n)** 0.5) # 최대 제한 속도
INF = int(1e9) # 임의 최대 카운트
dp = [[INF] * (LIMIT + 2) for _ in range(n + 1)]
dp[1][0] = 0 # 위치가 1일 때 속도 0으로 시작

stone = set() # 돌이 있는 위치 저장
for _ in range(m):
    stone.add(int(input()))

for i in range(2, n + 1):
    if i in stone: continue # 돌이 있는 곳에는 갈 수 없음
    for j in range(1, int(LIMIT + 1)):
        dp[i][j] = min(dp[i - j][j - 1], \
                        dp[i - j][j],\
                        dp[i - j][j + 1]) + 1

if min(dp[n]) == INF: print(-1)
else: print(min(dp[n]))
