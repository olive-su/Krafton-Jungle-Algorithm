# time : 6'

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True
        while queue:
            x = queue.popleft()
            for j in graph[x]:
                if not visited[j]:
                    visited[j] = True
                    queue.append(j)
        answer += 1

print(answer)
