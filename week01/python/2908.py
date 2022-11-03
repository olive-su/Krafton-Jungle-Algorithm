from audioop import reverse


n, m = map(reversed, map(list, input().split()))
print(max(int(''.join(n)), int(''.join(m))))
