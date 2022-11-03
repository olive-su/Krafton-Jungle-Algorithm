import sys

input = sys.stdin.readline
w, h = map(int, input().split())
t = int(input())

w_arr, h_arr = [0, w], [0, h]
w_val, h_val = 0, 0

for _ in range(t):
    d, l = map(int, input().split())
    if d: w_arr.append(l)
    else: h_arr.append(l)

w_arr.sort()
h_arr.sort()
w_val, h_val = w_arr[0], h_arr[0]

for w in range(1, len(w_arr)):
    w_val = max(w_val, w_arr[w] - w_arr[w - 1])

for h in range(1, len(h_arr)):
    h_val = max(h_val, h_arr[h] - h_arr[h - 1])

print(w_val * h_val)

