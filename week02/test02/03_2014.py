import sys
from heapq import *

input = sys.stdin.readline
k, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
priority_queue = []
for a in arr:
    heappush(priority_queue, a)

cnt = 1
while True:
    x = heappop(priority_queue)
    if cnt == n:
        print(x)
        break

    for a in arr:
        heappush(priority_queue, x * a)   
        if x % a == 0: break
    cnt += 1 


'''
############################
@ Try 1 : 시험 시간 종료로 실패
############################
import sys
from heapq import *

input = sys.stdin.readline
k, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
priority_queue = []
for a in arr:
    heappush(priority_queue, a)

cnt = 1
while True:
    x = heappop(priority_queue)
    if cnt == n:
        print(x)
        break

    for a in arr:
        heappush(priority_queue, x * a)   
        if x % a == 0: break
    cnt += 1 
'''
