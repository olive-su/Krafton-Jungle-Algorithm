# time : 10'

import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정렬
for i in range(1, n + 1):
    graph[i] = sorted(graph[i])

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]: dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if not visited[i]: 
                visited[i] = True
                queue.append(i)

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
