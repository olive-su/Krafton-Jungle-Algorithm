import sys
import math

input = sys.stdin.readline
n = int(input())
print(math.factorial(n))

# 직접 구현
# def factorial(n):
#     if n == 0:
#         return 1
    
#     return n * factorial(n - 1)
# 
# print(factorial(n))
