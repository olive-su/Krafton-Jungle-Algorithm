import sys

input = sys.stdin.readline

n = int(input())
fibo = [0, 1]

for i in range(2, n + 1):
    fibo.append(fibo[i - 1] + fibo[i - 2])

print(fibo[n])

# 시간초과(top-down)
# 
# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)