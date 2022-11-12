import sys
from heapq import *

input = sys.stdin.readline
p, position = [], []
answer, temp = 0, []
n = int(input())
for _ in range(n):
    p.append(sorted(list(map(int, input().split()))))
l = int(input())
for a, b in p: # 
    if b - a <= l: position.append((a, b))

n = len(position)
position.sort(key=lambda x : x[1])

for h, o in position:
    while temp and temp[0] < o - l:
        heappop(temp)
    heappush(temp, h)
    answer = max(answer, len(temp))

print(answer)