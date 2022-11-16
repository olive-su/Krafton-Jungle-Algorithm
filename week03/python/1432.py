import sys
from collections import deque
from heapq import *

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)] # 노드 연결 정보
outdegree = [0 for _ in range(n + 1)] # 진출 차수
node_num = [i for i in range(n + 1)] # 노드 번호 배열 (원본 : [0, 1, 2, 3, 4, 5, ...])

for i in range(1, n + 1):
    arr = list(input().rstrip())
    for a in range(n):
        if arr[a] == '1':
            graph[a + 1].append(i)
            outdegree[i] += 1

pq = [] 

for i in range(1, n + 1):
    if outdegree[i] == 0:
        heappush(pq, (-i, i))

num = n
cnt = 0
while pq:
    x = heappop(pq)[1]
    cnt += 1
    node_num[x] = num
    num -= 1
    for i in graph[x]:
        outdegree[i] -= 1
        if outdegree[i] == 0:
            heappush(pq, (-i, i))


if cnt != n: print(-1)
else: [print(node_num[i], end=' ') for i in range(1, n + 1)]

