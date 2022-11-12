import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def binary_search(start, end):
    answer = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in range(n):
            if arr[i] > mid: total += arr[i] - mid
        if total < m:
            end = mid -1
        else:
            start = mid + 1
            answer = mid
    return answer

print(binary_search(0, arr[-1])) # 최대로 나무 자를 수 있는 놈피