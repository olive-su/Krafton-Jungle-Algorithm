import sys

input = sys.stdin.readline
n = int(input())
total = 0

for i in range(1, n + 1):
    flag = 1
    if i < 10:
        total += 1
        continue
    s = str(i)
    gap = int(s[1]) - int(s[0]) # 등차
    for j in range(2, len(s)):
        if gap != int(s[j]) - int(s[j - 1]): # 등차가 다를경우 continue
            flag = 0
            break
    if flag:
        total += flag

print(total)