import sys

input = sys.stdin.readline
n = int(input())
answer = 0
order_ans = []

def hanoi(num, a, b, c):
    if num == 1:
        print(a, c)
        return 

    hanoi(num - 1, a, c, b)
    print(a, c)
    hanoi(num - 1, b, a, c)
    
print(2 ** n - 1)

if n <= 20: hanoi(n, 1, 2, 3)
