import sys

input = sys.stdin.readline
string = list(reversed(input().rstrip()))
bomb = list(input().rstrip())
slen, blen = len(string), len(bomb)
stack = []

def check_str():
    if len(stack) < len(bomb): return False
    for i in range(-1, -blen -1, -1):
        if stack[i] != bomb[i]: return False
    return True

while string or flag:
    if string:
        stack.append(string.pop())
    flag = check_str() 
    if flag:
        for _ in range(blen): stack.pop()

if stack: print(''.join(stack))
else: print('FRULA')