import sys

n = int(input())

if not n % 4:
    if n % 100 or not n % 400:
        sys.exit(print(1))

sys.exit(print(0))