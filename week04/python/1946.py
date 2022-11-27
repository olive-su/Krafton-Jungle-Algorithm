import sys

input = sys.stdin.readline

for _ in range(int(input())):
    employee, cnt = [], 1
    n = int(input())
    for _ in range(n):
        employee.append(tuple(map(int, input().split())))

    employee.sort()
    target = employee[0][1]

    for i in range(1, n):
        if target > employee[i][1]:
            cnt += 1
            target = employee[i][1]
    print(cnt)

