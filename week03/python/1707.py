import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# dfs
# group : 1 또는 -1
def dfs(v, n):
    visited[v] = n # 방문한 노드에 group 할당
    for i in graph[v]:
        if visited[i] == 0: # 아직 안 가본 곳이면 방문
            if not dfs(i, -n): # 현재 들어간 노드의 집합과 다른 집합으로 들어가야하기 때문
                return False
        elif visited[i] == visited[v]: # 방문한 곳인데, 그룹이 동일하면 False
            return False
    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)]
    visited = [0] * (V+1) # 방문한 정점 및 그룹 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    flag = True

    for i in range(1, V+1):
        if visited[i] == 0: # 방문한 정점이 아니면, dfs 수행
            flag = dfs(i, 1)
            if not flag:
                break

    print('YES' if flag else 'NO')