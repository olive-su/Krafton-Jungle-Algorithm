# 실행 속도를 비약적으로 줄이기 위해서 절반으로 나눈 값으로 연산을 수행함

def divide_and_conquer(a, b):
    if b == 1:
        return a % c

    rst = divide_and_conquer(a, b // 2)
    
    if b % 2 == 0:
        return rst * rst % c
    else:
    	return rst * rst * a % c
        
a, b, c = map(int, input().split())
print(divide_and_conquer(a, b))