import sys

n = int(input())

def num_cycle(num, cnt):
    rst, lnum = 0, num % 10
    while num > 0 :
        rst += (num % 10)
        num //= 10
    
    rst = int(str(lnum) + str(rst % 10))

    if rst == n:
        sys.exit(print(cnt + 1))
    else:
        num_cycle(rst, cnt + 1)

num_cycle(n, 0)    