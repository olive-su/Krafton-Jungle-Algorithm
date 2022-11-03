idx, answer = 0, 0

for i in range(9):
    t = int(input())
    if answer < t:
        idx = i + 1
        answer = t 

print(answer)
print(idx)
