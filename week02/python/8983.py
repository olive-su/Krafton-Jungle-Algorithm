import sys

'''
m, n, l
사대 m
동물 n
O(nlgn)
'''
input = sys.stdin.readline
m, n, l = map(int, input().split())
gun = sorted(list(map(int, input().split())))
answer = 0

# 현재 동물이 사정거리 내에 있는지 검사
for _ in range(n):
    x, y = map(int, input().split()) # x, y
    start, end = 0, m - 1
    if y > l: continue # 전혀 도달할 수 없는 사정거리
    while start <= end:
        mid = (start + end) // 2
        if abs(gun[mid] - x) + y <= l:
            answer += 1
            break
        if x < gun[mid]:
            end = mid - 1
        else:
            start = mid + 1

print(answer)
