import sys
from itertools import combinations

input = sys.stdin.readline
arr = []
for _ in range(9):
    a = int(input())
    arr.append(a)

comb = list(combinations(arr, 7))
for c in comb:
    if sum(c) == 100:
        rst = sorted(list(c))
        [print(r, end='\n') for r in rst]
        sys.exit()
