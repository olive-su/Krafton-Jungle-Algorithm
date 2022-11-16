'''
@indegree : 차수
@graph : 그래프 연결 관계
@cnt : 결과 배열
@basic : 기본 부품인지 여부
'''

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
cnt = [0] * (n + 1) # 전체 부품의 필요 개수
basic = [True] * (n + 1) # 기본 부품 여부

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a를 만들기 위해 b가 c개 필요함
    indegree[b] += 1
    basic[a] = False # 기본 부품인지 bool값 삽입

def topology_sort():
    q = deque()

    # 진입 차수가 0이면 큐에 추가(완제품)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            cnt[i] = 1 # 초기 개수 1로 초기화
            q.append(i)
    
    while q:
        start = q.popleft()

        for i in graph[start]:
            end, w = i # 도착 노드, 개수
            cnt[end] += cnt[start] * w
            indegree[end] -= 1
            if indegree[end] == 0:
                q.append(end)
    
topology_sort()

for i in range(1, n + 1):
    if basic[i]: print(i, cnt[i], sep=' ')
