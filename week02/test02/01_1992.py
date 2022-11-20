import sys

input = sys.stdin.readline
n = int(input())
graph, answer = [], []
dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]

for _ in range(n):
    graph.append(list(input().rstrip()))

# 색이 모두 동일한 지 판단
def validation(n, x, y):
    color = graph[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[i][j] != color: return False
    return color

def quad_tree(n, x, y):
    for i in range(4):
        nx = x + dx[i] * n
        ny = y + dy[i] * n 
        rst = validation(n, nx, ny)
        if rst == False:
            answer.append('(')
            quad_tree(n // 2, nx, ny)
            answer.append(')')
        else:
            answer.append(rst)

if validation(n, 0, 0) != False: sys.exit(print(graph[0][0]))
else: quad_tree(n // 2, 0, 0)

print('(', ''.join(answer), ')', sep='')