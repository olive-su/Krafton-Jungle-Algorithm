# boj. 1388
# time : 23'

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0

for _ in range(n):
    board.append(list(input().rstrip()))


def bfs(y, x, shape):
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        if shape == '|':
            if y + 1 < n and board[y + 1][x] == shape and not visited[y + 1][x]:
                visited[y + 1][x] = True
                queue.append((y + 1, x))
        else:
            if x + 1 < m and board[y][x + 1] == shape and not visited[y][x + 1]:
                visited[y][x + 1] = True
                queue.append((y, x + 1))

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            answer += 1
            bfs(i, j, board[i][j])

print(answer)
