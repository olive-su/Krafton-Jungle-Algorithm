import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

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

def dfs(vertex):
    cnt = 0
    for j in nodes[vertex]:
        if in_out[j]:
            cnt += 1
        else:
            if not visited[j]:
                visited[j] = True
                cnt += dfs(j)
    return cnt

for i in range(1, n + 1):
    if in_out[i]:
        for j in nodes[i]:
            if in_out[j]: answer += 1
    else:
        if not visited[i]:
            visited[i] = True
            rst = dfs(i)
            answer += rst * (rst - 1)

print(answer)