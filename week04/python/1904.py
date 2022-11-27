import sys

input = sys.stdin.readline

n = int(input())
fibo = [0, 1, 2]

for i in range(3, n + 1):
    fibo.append((fibo[i - 1] + fibo[i - 2]) % 15746)

print(fibo[n])