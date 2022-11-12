import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
arr = deque(list(map(str, range(1, n + 1))))
answer = []

i = 1
while arr:
    if i == k:
        answer.append(arr.popleft())
        i = 0
    else:
        arr.append(arr.popleft()) 
    i += 1

print('<',', '.join(answer), '>', sep='')