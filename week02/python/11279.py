import sys
from heapq import *

# max heap 구현을 위해서 (-n, n) 형태로 데이터 삽입
input = sys.stdin.readline
priority_queue = []
for _ in range(int(input())):
    command = int(input())
    if command == 0:
        if len(priority_queue) == 0: print(0)
        else: print(heappop(priority_queue)[1])
    else: heappush(priority_queue, (-command, command))
