# time : 47'

import sys
from collections import deque

'''
. : 빈 곳
* : 물 차있음
x : 돌
d : 굴
s: 고슴도치
'''

# 물, 고슴도치 둘 다 이동
input = sys.stdin.readline
r, c = map(int, input().split())
graph = []
water = [[-1] * c for _ in range(r)] # 물 이동 경로
hedge = [[-1] * c for _ in range(r)] # 고슴도치 이동 경로
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
time = 0

for _ in range(r):
    graph.append(list(input().rstrip())) 

def bfs_water(x, y):
    queue = deque([(x, y)])
    water[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if graph[ny][nx] == '.' or graph[ny][nx] == 'S': 
                    if water[ny][nx] == -1 or water[ny][nx] > water[y][x] + 1:
                        water[ny][nx] = water[y][x] + 1
                        queue.append((nx, ny))

def bfs_hedge(x, y):
    queue = deque([(x, y)])    
    hedge[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if graph[ny][nx] == '.' and hedge[ny][nx] == -1:
                    if water[ny][nx] == -1 or (water[ny][nx] > hedge[y][x] + 1):
                        hedge[ny][nx] = hedge[y][x] + 1
                        queue.append((nx, ny))
                if graph[ny][nx] == 'D':
                    return hedge[y][x] + 1
    return 0


for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            bfs_water(j, i)

# 'S'는 전체 맵 중 하나만 존재하므로 바로 answer에 담아줘도 된다.
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            answer = bfs_hedge(j, i)

if not answer: print('KAKTUS')
else: print(answer)

