# time : 35'

import sys

input = sys.stdin.readline
n = int(input())
max_v, min_v = -1e9, 1e9
arr = input().split()
operand = list(map(list, zip(['+' , '-', '*', '/'], list(map(int, input().split())))))

def dfs(idx, total):
    global max_v, min_v
    if idx == n:
        max_v = max(max_v, total)
        min_v = min(min_v, total)
        return
    
    for i in range(4):
        if operand[i][1]:
            operand[i][1] -= 1
            cal = int(eval(str(total) + operand[i][0] + arr[idx]))
            dfs(idx + 1, cal)
            operand[i][1] += 1

dfs(1, int(arr[0]))

print(max_v)
print(min_v)
