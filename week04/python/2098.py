import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(sys.stdin.readline())
w = [list((map(int, input().split()))) for _ in range(n)] # 각 도시의 가중치 값
size = 2 ** (n - 1) 
dp = [[INF] * size for _ in range(n)]

def count(route):
    cnt = 0
    for i in range(1, n):
        if route & (1 << i - 1) != 0:
            cnt += 1
    return cnt

def is_in(i, route):
    if route & (1 << i - 1) != 0:
        return True
    else:
        return False

def get_minimum(i, route):
    minimum_dist = INF
    for j in range(1, n):
        if is_in(j, route):
            before_route = route & ~(1 << j - 1)
            dist = w[i][j] + dp[j][before_route]
            if minimum_dist > dist:
                minimum_dist = dist
    return minimum_dist

for i in range(n):
    for j in range(n):
        if not w[i][j]:
            w[i][j] = INF

for i in range(1, n):
    dp[i][0] = w[i][0]

for k in range(1, n - 1):
    for route in range(1, size):
        if count(route) == k:
            for i in range(1, n):
                if not is_in(i, route):
                    dp[i][route] = get_minimum(i, route)

# 결국 여기까지는 0에 도착하는 경우는 채워진 상태

dp[0][size - 1] = get_minimum(0, size - 1)
# 0에서 출발하는 경우는 아직 안채워짐

print(dp[0][size - 1])

