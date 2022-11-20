# time 9' 21"

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
tree, visited = [], []
answer = 0
dx = [[-1, 0], [-1, 0], [0, 1], [0, 1]]
dy = [[0, 1], [0, -1], [-1, 0], [1, 0]]

for _ in range(n):
    tree.append(list(map(int, input().split())))
    visited.append([False] * m)

def backtracking(cnt):
    global answer

    answer = max(answer, cnt)
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                for k in range(4):
                    dxf, dyf = j + dx[k][0], i + dy[k][0]
                    dxs, dys = j + dx[k][1], i + dy[k][1] 
                    if 0 <= dyf < n and 0 <= dxf < m and 0 <= dys < n and 0 <= dxs < m:
                        visited[dyf][dxf] = True
                        visited[dys][dxs] = True
                        visited[i][j] = True
                        val = (tree[i][j] * 2) + tree[dys][dxs] + tree[dyf][dxf]
                        backtracking(cnt + val)
                        visited[dyf][dxf] = False
                        visited[dys][dxs] = False
                        visited[i][j] = False


backtracking(0)