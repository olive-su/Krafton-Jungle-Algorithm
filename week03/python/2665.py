import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = []
visited = [[-1] * n for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

for i in range(n):
    graph.append(list(input().rstrip()))

def bfs(y, x):
    queue = deque([(y, x)])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == -1:
                    if graph[ny][nx] == '1': 
                        visited[ny][nx] = visited[y][x]
                        queue.appendleft((ny, nx))
                    else: 
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))
                    
    print(visited)

visited[0][0] = 0

bfs(0, 0)

print(visited[n-1][n-1])