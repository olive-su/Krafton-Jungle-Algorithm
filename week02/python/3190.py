import sys
from collections import deque

'''
@board : 뱀 위치 표시
@apple : 사과 위치 표시
@dx, dy : 방향 벡터 (우, 하, 좌, 상 - 시계 방향)
@d_list : 방향 명령어
@snake : 현재 뱀의 위치(머리 ~ 꼬리)
@time : 현재 시간(반복문 횟수에 따라 1씩 증가)
@x, y, d : 현재 머리 좌표 x, y, 현재 방향(우, 하, 좌, 상) 
'''
input = sys.stdin.readline
n = int(input())
board = [([False]  * n) for _ in range(n)]
apple = [([False]  * n) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d_list = deque([])
snake = deque([(0, 0)])
time = 1

board[0][0] = True # 현재 뱀 머리 위치
for _ in range(int(input())):
    y, x = map(int, input().split())
    apple[y - 1][x - 1] = True

for _ in range(int(input())):
    a, b = input().split() # (time, direction)
    d_list.append((int(a), b)) 

x, y, d = 0, 0, 0
while True:
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and not board[ny][nx]:
        if apple[ny][nx]: apple[ny][nx] = False
        else:
            cx, cy = snake.popleft()
            board[cy][cx] = False
        snake.append((nx, ny))
        board[ny][nx] = True
    else: break

    # t초 뒤, 방향 전환이므로 다음 루프에 방향 전환을 시켜주기 위해 해당 조건문을 뒤로 뺌
    if d_list and d_list[0][0] == time:
        if d_list[0][1] == 'D': d = (d + 1) % 4 # 우회전
        else: d = (d + 3) % 4 # 좌회전 (+3은 음수 방지)
        d_list.popleft()
    
    x, y = nx, ny
    time += 1

print(time)