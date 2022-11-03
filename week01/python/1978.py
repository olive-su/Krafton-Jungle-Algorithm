import sys
import math

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
max_v = max(arr)
answer = 0

# ver1 : 단순 소수 비교
def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

for a in arr:
    answer += is_prime(a)

print(answer)

# ver2 : 에라토스테네스의 체
# answer = 0

# def eratos(n):
#     primes = [True] * (n + 1)
#     primes[0], primes[1] = False, False

#     for i in range(2, int(math.sqrt(n)) + 1):
#         if primes[i]:
#             num = 2
#             while num * i <= n:
#                 primes[num * i] = False
#                 num += 1
    
#     return primes

# primes = eratos(max_v)

# for a in arr:
#     answer += primes[a]

# print(answer)

