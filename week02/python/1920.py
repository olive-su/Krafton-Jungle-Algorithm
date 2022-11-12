import sys

input = sys.stdin.readline
n = int(input())
src_arr = sorted(list(map(int, input().split())))
m = int(input())
target_arr = list(map(int, input().split()))

for i in range(m):
    target = target_arr[i]
    start, end, flag = 0, n - 1, 0
    while start <= end:
        mid = (start + end) // 2
        if target == src_arr[mid]: 
            flag = 1
            break
        elif target < src_arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    print(flag)

