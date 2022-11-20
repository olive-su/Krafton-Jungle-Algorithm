import sys
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
times = [0] * (n + 1)
result = [0] * (n + 1)

q = deque()

for i in range(1, n + 1):
    command = list(map(int, input().split()))
    times[i] = command[0]
    if command[1] == -1: 
        q.append(i) # 시작 정점
        result[i] = times[i]
    for c in range(1, len(command) - 1):    
        if command[c] == -1: break
        graph[command[c]].append(i)
        indegree[i] += 1

total = 0

while q:
    x = q.popleft()

    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
            result[i] = result[x] + times[i]

[print(result[r]) for r in range(1, n + 1)]

