'''
스택에서 pop을 수행하면서 높이가 낮은 탑이 등장하면 해당 탑에 높이를 맞춤
'''

import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))
while arr[0]:
    rst, tmp = 0, 0
    n, arr = arr[0], arr[1:]
    answer = 0
    
    stack = []
    for i in range(n):
        cnt, flag = 0, False
    
        while stack and stack[-1][0] > arr[i]:
            flag = True
            s = stack.pop()
            answer = max(answer, s[0] * (i - s[1]))
        if flag: stack.append((arr[i], s[1]))
        stack.append((arr[i], i))
    
    while stack:
        s = stack.pop()
        answer = max(answer, s[0] * (n - s[1]))
    
    print(answer)

    arr = list(map(int, input().split()))