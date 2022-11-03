import sys
import math

input = sys.stdin.readline
t = int(input())

# 문제에서 제시된 인풋 최대값이 10000
primes = [True] * 10001
primes[0], primes[1] = False, False

for i in range(2, 101):
    if primes[i] == True:
        num = 2
        while num * i <= 10000:
            primes[num * i] = False
            num += 1

for _ in range(t):
    n = int(input()) 

    for i in range(n//2, n + 1):
        if primes[i] and primes[n - i]:
            print(n - i, i)
            break
