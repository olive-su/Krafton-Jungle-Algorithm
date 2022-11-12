import sys

input = sys.stdin.readline
n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

cnt = [0, 0]
dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]

# 자른 종이 조각이 모두 같은 색인지 판별
def validation(num, x, y):
    color = board[y][x]
    for i in range(y, y + num):
        for j in range(x, x + num):
            if color != board[i][j]:
                return -1
    
    return color

# 4등분해서 확인
def check(num, x, y):
    rst = validation(num, x, y)
    if rst == -1:
        for i in range(4):
            check(num // 2, x + num // 2 * dx[i], y + num // 2 * dy[i])
    else: cnt[rst] += 1

check(n, 0, 0)
print(cnt[0])
print(cnt[1])
