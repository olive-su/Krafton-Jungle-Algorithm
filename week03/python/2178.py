# time : 10'

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph, visited = [], [[0] * m for _ in range(n)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

for _ in range(n):
    graph.append(list(input().rstrip()))

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == '1' and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx, ny))

visited[0][0] = 1
bfs(0, 0)
print(visited[n - 1][m - 1])
