import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    ever = sum(arr[1:]) / arr[0]
    num = 0

    for a in range(1, arr[0] + 1):
        if arr[a] > ever:
            num += 1
    
    r = (num / arr[0])  * 100
    print('{:.3f}%'.format(r))
