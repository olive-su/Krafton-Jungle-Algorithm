import sys

input = sys.stdin.readline

n, m = map(int, input().split())

heavy, light = [[] * (n + 1) for _ in range(n + 1)], [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    heavy[b].append(a) # 나보다 큰 애들
    light[a].append(b) # 나보다 작은 애들

def dfs(arr, num, cnt):
    for i in arr[num]:
        if not visited[i]:
            visited[i] = True
            cnt = dfs(arr, i, cnt + 1)
    return cnt

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if dfs(heavy, i, 0) > n // 2:
        visited[i] = True
        answer += 1

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if dfs(light, i, 0) > n // 2:
        visited[i] = True
        answer += 1

print(answer)


