# pop() 보다 큰 탑이 있을 경우 해당 탑이 수신
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n
stack = [(0, arr.pop(0))]
arr.reverse()

i = 1
while arr: 
    top = arr.pop()
    # 현재 top 보다 작은 값이 가장 가까이에 있으면 모두 pop
    # 전부 가려지게 됨
    while stack and stack[-1][1] <= top:
        stack.pop()
    # 스택이 비었을 경우
    if not len(stack): answer[i] = 0
    else: answer[i] = stack[-1][0] + 1
    stack.append((i, top))
    i += 1

[print(a, end=' ') for a in answer]
