import sys

input = sys.stdin.readline
n = int(input())
arr = []
answer, h = 0, 0

for _ in range(n):
    arr.append(int(input()))

for _ in range(n):
    stick = arr.pop()
    if h < stick:
        h = stick
        answer += 1

print(answer)
