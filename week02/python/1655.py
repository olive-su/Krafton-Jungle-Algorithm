import sys
from heapq import *

input = sys.stdin.readline
n = int(input())
queue_left, queue_right = [], []

for i in range(n):
    num = int(input())
    if not queue_left:
        heappush(queue_left, (-num, num))
    else:
        if queue_left[0][1] > num:
            heappush(queue_left, (-num, num))
        else:
            heappush(queue_right, num)
    if len(queue_left) - len(queue_right) > 1:
        heappush(queue_right, heappop(queue_left)[1])
    elif len(queue_left) - len(queue_right) < 0:
        qr = heappop(queue_right)
        heappush(queue_left, (-qr, qr))
    print(queue_left[0][1])
