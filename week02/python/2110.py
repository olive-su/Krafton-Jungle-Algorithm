import sys

input = sys.stdin.readline
n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

def binary_search():
    answer = 0
    start, end = 0, arr[-1]
    while start <= end:
        mid = (start + end) // 2
        l_house = arr[0] # 이전 집과의 간격 측정을 위한 포인터
        cnt = 1
        for i in range(1, n):
            if arr[i] - l_house >= mid:
                cnt += 1
                l_house = arr[i]
        if cnt < c:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer

print(binary_search())


