import sys

input = sys.stdin.readline
multi = 1
for _ in range(3):
    multi *= int(input())

for i in range(10):
    print(multi.count(str(i)))