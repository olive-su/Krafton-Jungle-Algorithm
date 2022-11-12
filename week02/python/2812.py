import sys

input = sys.stdin.readline
n, k = map(int, input().split())
gap = n - k
n_arr = list(map(int, list(input().rstrip())))
stack = []

for i in range(n):
    target = n_arr[i]
    while k > 0 and stack and stack[-1] < target:
        stack.pop()
        k -= 1
    stack.append(target)

[print(stack[i], end='') for i in range(gap)]