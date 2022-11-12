# time : 6' 

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
e = int(input())
computers = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(e):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

queue = deque([1])
visited[1] = True
while queue:
    x = queue.popleft()
    for i in computers[x]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
    answer += 1
    
print(answer - 1)