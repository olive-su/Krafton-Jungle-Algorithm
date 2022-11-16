import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
result = [0] * (n + 1)
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    reverse_graph[b].append((a, c))
    indegree[b] += 1

start, end = map(int, input().split())


def topology_sort():
    global cnt 

    q = deque([start])
    
    while q:
        left = q.popleft()

        for right, t in graph[left]:
            indegree[right] -= 1
            result[right] = max(result[right], result[left] + t)
            if indegree[right] == 0:
                q.append(right)
    
    q.append(end)
    while q:
        right = q.popleft()

        for left, t in reverse_graph[right]:
            if result[right] - result[left] == t: # 나까지의 경로 값 - 나한테 오는 아이의 경로 값이 간선 가중치와 동일 시
                cnt += 1
                if not visited[left]:
                    q.append(left)
                    visited[left] = True
                        
topology_sort()

print(result[end])
print(cnt)


