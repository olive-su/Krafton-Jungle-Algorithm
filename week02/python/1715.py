# 그리디 : 카드 개수가 적은 것부터

import sys
from heapq import *

input = sys.stdin.readline
cards = []
answer = 0
for _ in range(int(input())):
    heappush(cards, int(input()))

while len(cards) > 1:
    a, b = heappop(cards), heappop(cards)
    heappush(cards, a + b)
    answer += a + b

print(answer)
