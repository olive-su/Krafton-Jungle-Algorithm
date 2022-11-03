# ver1
# t = int(input())
# for _ in range(t):
#     n, string = input().split()
#     for s in string:
#         for _ in range(int(n)):
#             print(s, end='')
#     print()

# ver2
for _ in range(int(input())):
    a = input().split()
    print(''.join(list(map(lambda x:x * int(a[0]), a[1]))))