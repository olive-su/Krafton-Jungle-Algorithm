import sys

input = sys.stdin.readline()
x, y, w, h = map(int, input.split())

rst = min(x, y, w - x, h)

rst = min(rst, w - x)
rst = min(rst, h - y)
print(rst)