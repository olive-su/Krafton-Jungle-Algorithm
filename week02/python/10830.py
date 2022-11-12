import sys
from copy import deepcopy

input = sys.stdin.readline
n, b = map(int, input().split())
origin, matrix = [], []

for i in range(n):
    origin.append(list(map(int, input().split())))
    matrix.append(origin[-1])

def matrix_pow(l_matrix, r_matrix):
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                total += (l_matrix[i][k] * r_matrix[k][j])
            temp[i][j] = total % 1000
    return temp

def divide_and_conquer(b):
    temp = [[0] * n for _ in range(n)]
    if b == 1:
        for i in range(n):
            for j in range(n):
                temp[i][j] = matrix[i][j]
        return temp

    rst = divide_and_conquer(b // 2)

    if b % 2 == 0:
        return matrix_pow(rst, rst)
    else:
        return matrix_pow(matrix_pow(rst, rst), origin)

        return matrix_pow(matrix_pow(rst, origin), rst)

matrix = divide_and_conquer(b)

for a in matrix:
    for b in a: print(b, end=' ')
    print()