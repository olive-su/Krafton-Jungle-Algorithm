import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    money = int(input())

    dp = [0] * (money + 1)
    for i in coin:
        if i <= money:
            dp[i] += 1
            for j in range(i + 1, money + 1):
                dp[j] += dp[j - i]
    
    print(dp[money])


