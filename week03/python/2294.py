'''
# DP
import sys
r = sys.stdin.readline

N, K = map(int, r().split())
coins = sorted([int(r()) for _ in range(N)])

arr = [10001] * (K+1)
arr[0] = 0

for i in range(N):
    for j in range(coins[i], K+1):
        arr[j] = min(arr[j], arr[j-coins[i]] + 1)

arr[-1] = arr[-1] if arr[-1] != 10001 else -1
print(arr[-1])
'''

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 중복된 코인 제거
coins = set()
for _ in range(n):
    coins.add(int(input()))
coins = list(coins)
visited = [False for _ in range(k + 1)] # 코인 방문 배열

def bfs(coins, k):
    queue = deque()
    for coin in coins:
        if coin < k:
            queue.append([coin, 1])
            visited[coin] = True

    while queue:
        c, cnt = queue.popleft()
        if k == c: # 가장 먼저 개수가 k가 되는 경우가 최소값이므로 바로 리턴
            print(cnt)
            break
        for coin in coins: # 모든 경우 다 돌림
            sum_c = c + coin
            sum_cnt = cnt + 1
            if sum_c > k:
                continue
            elif sum_c <= k and not visited[sum_c]:
                visited[sum_c] = True
                queue.append([sum_c, sum_cnt])
            
    if c != k: # k를 만족할 수 없는 경우
        print('-1')

bfs(coins,k)

