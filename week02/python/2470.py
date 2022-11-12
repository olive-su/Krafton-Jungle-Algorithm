import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
val, answer = 1e18, (0, 0)

start, end = 0, n - 1
while start < end:
    t = abs(arr[start] + arr[end]) 
    if val > t:
        val = t
        answer = (arr[start], arr[end])
    a = abs(arr[start + 1] + arr[end])
    b = abs(arr[end - 1] + arr[start])
    if a < b: start = start + 1
    else: end = end - 1

print(answer[0], answer[1], sep=' ')
