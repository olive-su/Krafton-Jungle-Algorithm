# boj. 2078
# time : 14'

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
left_cnt, right_cnt = 0, 0

# 트리 역방향부터 순회
def inf_binary_tree(a, b):
    global left_cnt, right_cnt

    if a == 1 and b == 1:
        return
    if a == 1:
        right_cnt += b - 1
        return
    if b == 1:
        left_cnt += a - 1
        return
    if a > b:
        left_cnt += a//b
        inf_binary_tree(a % b, b)
    else:
        right_cnt += b//a
        inf_binary_tree(a, b % a)

inf_binary_tree(a, b)
print(left_cnt, right_cnt)


'''
######################
@ Try 1 : 메모리 초과
######################

import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())
nodes = []

queue = deque([[(1, 1), 0, 0]]) # (a, b), left_cnt, right_cnt
while queue:
    num, l_cnt, r_cnt = queue.popleft()
    if num == (a, b):
        sys.exit(print(l_cnt, r_cnt, sep=' '))
    l_child = (sum(num), num[1])
    r_child = (num[0], sum(num))
    queue.append([l_child, l_cnt + 1, r_cnt])
    queue.append([r_child, l_cnt, r_cnt + 1])
'''