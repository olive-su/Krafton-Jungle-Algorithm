import sys

a, b, v = map(int, sys.stdin.readline().split())
c = (v-b)/(a-b)
if c == int(c):
    print(int(c))
else:
    # 나머지가 있음 -> 그 다음날 낮에 정상 도착 가능
    print(int(c)+1)