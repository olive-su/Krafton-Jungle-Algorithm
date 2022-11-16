import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(y, x):
    cnt = 0
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if not graph[ny][nx]: cnt += 1
            else:
                if not visited[ny][nx]:
                    visited[ny][nx] = True    
                    dfs(ny, nx)
    graph[y][x] = max(0, graph[y][x] - cnt)

while True:
    flag = 0
    visited = [[0] * m for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] and not visited[i][j]:
                visited[i][j] = True    
                dfs(i, j)
                flag += 1

    print(graph)
    if not flag:
        print(0)
        break # 빙산이 다 녹을 때 까지 x
    elif flag > 1:
        print(year)
        break
    year += 1