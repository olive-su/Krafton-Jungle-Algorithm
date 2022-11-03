import sys

input = sys.stdin.readline
n = int(input())
arr = []
visited = [False] * n # 방문처리 배열
answer = 1e9 

for _ in range(n):
    arr.append(list(map(int, input().split())))

'''
@init : 맨 처음 여행 시작 도시
@node : 도착한 도시
@cnt : 방문한 도시 수
@rst : 방문한 도시 거리
'''
def backtracking(init, node, cnt, rst):
    global answer

    if cnt == n:
        if arr[node][init]: # 맨 처음 노드로 돌아갈 수 있는지 검사
            answer = min(answer, rst + arr[node][init]) # answer 값 중 최솟값
        return
    
    for i in range(n):
        if not visited[i] and arr[node][i]: # 해당 도시를 방문하지 않았고 방문이 가능한 경우만 방문
            visited[i] = True # 방문처리
            backtracking(init, i, cnt + 1, rst + arr[node][i])
            visited[i] = False

for i in range(n): # 시작 노드 결정
    visited[i] = True
    backtracking(i, i, 1, 0)
    visited[i] = False

print(answer)