# time : 9' 30"

import sys
sys.setrecursionlimit(10**9) # 재귀 최대 깊이 미설정시, 시간 초과

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1) # 아직 부모 노드 미확정 시, 0

for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

def dfs(num):
    for i in tree[num]:
        if not parent[i]:
            parent[i] = num
            dfs(i)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])
