import sys
from collections import Counter, defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())
products = input().split()
answer = 0
products_Counter = sorted(Counter(reversed(products)).items(), key=lambda x : x[1])
products_cnt, occupied = {}, defaultdict(bool)
for p in products_Counter: products_cnt[p[0]] = p[1]

def calc_priority(now): # -인덱스 -> 우선 순위
    priority = []
    p_items = products_cnt.items()

    for p_name, p_cnt in p_items:
        if not p_cnt: idx = 101
        else: idx = products[now:].index(p_name)
        priority.append((p_name, -idx))
    
    priority.sort(key=lambda x : x[1]) # 우선 순위 순 정렬
    return priority


for i in range(k):
    e = products[i]
    if occupied[e]:
        products_cnt[e] -= 1
        continue
    if n > 0: n -= 1
    else:
        priority = calc_priority(i)
        for name, order in priority:
            if occupied[name]:
                occupied[name] = not occupied[name]
                answer += 1
                break
    occupied[e] = not occupied[e]
    products_cnt[e] -= 1

print(answer)