#boj. 1379

import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
arr, room = [], []

for _ in range(n):
    num, st, et = map(int, input().split())
    arr.append((num, st, et))

arr.sort(key=lambda x : x[1]) # 시작 시간 순 정렬

while len(arr) > 0:
    now_num, now_st, now_et = heappop(arr)

print(arr)


