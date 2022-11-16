from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
flag, zeros_cnt = 0, 0
tom = []  # 익은 토마토의 위치를 저장하기 위한 배열
# 상자의 상태를 저장하기 위해 빈 배열 하나 생성
tomatos = [[[] for j in range(n)] for i in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 상자의 상태 -> 배열에 저장
for i in range(h):
    for j in range(n):
        input = list(map(int, stdin.readline().split()))
        tomatos[i][j] = input
        if 0 in input:
            flag = 1  # 덜익은 토마토가 있는 경우, 없으면 flag = 0 유지
        for k in range(len(input)):
            if input[k] == 1:  # 익은 토마토의 위치를 tom에 담음
                tom.append((i, j, k))
        zeros_cnt += input.count(0)  # 익지 않은 토마토의 개수를 셈


def bfs(arr):
    queue = deque()
    # cnt : 토마토가 다 익을때까지 걸리는 시간
    # turn : 안 익은 토마토를 익힌 횟수
    cnt, turn = 0, 0
    for i in arr:  # 익은 토마토의 위치를 큐에 삽입
        queue.append((i[0], i[1], i[2]))
    while queue:
        queue_list = []
        while queue:  # queue_list에 현재 익은 토마토들의 위치를 삽입
            queue_list.append(queue.popleft())
        for i in queue_list:  # 현재 익은 토마토들을 모두 방문하여 인근 토마토들로 익힘도 확산
            x, y, z = i[0], i[1], i[2]
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                # 범위를 벗어날 경우 반복문 탈출
                if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                    continue
                if tomatos[nx][ny][nz] == 0:
                    queue.append((nx, ny, nz))
                    tomatos[nx][ny][nz] = 1
                    turn += 1  # 토마토가 익을 경우 turn + 1
        cnt += 1
        # 맨 처음에 세둔 안익은 토마토의 개수와 익은 토마토의 개수가 같을 경우 while문 종료
        if zeros_cnt == turn:
            break
    return cnt


cnt = bfs(tom)
for i in range(h):
    for j in range(n):
        for k in range(m):
            # '안익은 토마토가 있는 경우' => '토마토가 모두 익지 못하는 상황'
            if tomatos[i][j][k] == 0:
                print(-1)
                exit(0)
if flag:
    print(cnt)
else:  # 저장될 때부터 토마토가 모두 익어있는 상태
    print(0)
