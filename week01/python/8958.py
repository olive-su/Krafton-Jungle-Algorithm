t = int(input())

for _ in range(t):
    score = input()
    total, rst = 0, 0
    for i in score:
        if i == 'O':
            total += 1
            rst += total
        else: total = 0
    print(rst)