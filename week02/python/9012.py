import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    stack = 0
    vps = input().rstrip()
    flag = 'YES'
    for i in vps:
        if i == '(': stack += 1
        else: stack -= 1
        if stack < 0: 
            flag = 'NO'
            break
    if not stack == 0: flag = 'NO'

    print(flag)
