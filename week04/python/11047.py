import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins, answer = [], 0
for _ in range(n):
    coins.append(int(input()))

coins.reverse()
for c in coins:
    if k >= c:
        answer += k // c
        k %= c

print(answer)