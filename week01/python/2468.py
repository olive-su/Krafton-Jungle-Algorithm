import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph, visited = [], [[False for _ in range(n)] for _ in range(n)]
max_h, answer = 0, 0

for _ in range(n):
    graph.append(list(map(int, input().split())))
    max_h = max(max_h, max(graph[-1]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h, visited):
    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 좌표 범위 내
                if graph[ny][nx] > h and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

for h in range(max_h):
    rst = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]: 
                bfs(j, i, h, visited)
                rst += 1
    answer = max(answer, rst)    

print(answer)
