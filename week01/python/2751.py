import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

[print(heapq.heappop(arr)) for _ in range(n)]
