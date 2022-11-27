calc = input().rstrip().split('-')
tmp = []

for i in calc:
    rst = 0
    for j in i.split('+'):
        rst += int(j)
    tmp.append(str(rst))

print(eval('-'.join(tmp)))
