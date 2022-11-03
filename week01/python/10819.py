import sys
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
comb = list(permutations(arr, n))
answer = 0

def gap(target):
    rst = 0
    for i in range(n-1):
        rst += abs(target[i] - target[i + 1])
    return rst

for c in comb:
    answer = max(answer, gap(c))

print(answer)