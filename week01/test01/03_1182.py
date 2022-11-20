import sys
from itertools import combinations

input = sys.stdin.readline
answer = 0
n, s = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, n + 1):
    comb = list(combinations (arr, i))
    for c in comb:
        if sum(c) == s:
            answer += 1

print(answer)