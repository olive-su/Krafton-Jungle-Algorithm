import sys

input = sys.stdin.readline
s = input().rstrip()
p = input().rstrip()

j = 0
for i in range(len(s)):
    if s[i] == p[j]: j += 1
    else: j = 0
    if j == len(p): sys.exit(print(1))

print(0)
