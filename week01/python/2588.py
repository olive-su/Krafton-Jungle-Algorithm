from math import pow

a = int(input())
b = int(input())
total = 0


for i in range(3):
    rst = (b % 10) * a # 일의 자리 숫자 남기는 코드
    b //= 10 # 다음 로직을 위해 b값 변경
    total += rst * pow(10, i) # 일의 자리 숫자니까, 자릿수 곱해주기
    print(rst)

print(round(total))