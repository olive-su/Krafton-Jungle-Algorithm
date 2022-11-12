'''
시작, 끝 : 실내
산책 중 실내가 있으면 안됨
매일 다른 산책 경로
n개의 장소를 N-1개의 경로
'''

# time : 30'

import sys

input = sys.stdin.readline
n = int(input())
in_out = list(map(int, list(input().rstrip())))
in_out.insert(0, -1)
nodes = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(n - 1):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)

def dfs(start):
    global answer

    for j in nodes[start]:
        if not visited[j]:
            if in_out[j]: 
                answer += 1 # 실내면 종료
            else:
                visited[j] = True
                dfs(j)
                visited[j] = False
        
dfs(1)

print(answer)

