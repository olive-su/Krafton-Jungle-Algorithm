import sys

input = sys.stdin.readline
n = int(input())
words = []
for _ in range(n):
    words.append(input().rstrip())

words = list(set(words))
words.sort(key=str.lower)
words.sort(key=len)
[print(w, end='\n') for w in words]