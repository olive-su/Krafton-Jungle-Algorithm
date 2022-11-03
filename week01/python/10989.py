# 계수정렬

import sys
n = int(sys.stdin.readline())
cnt = [0] * (10001) # max_val 대로 리스트 생성
for _ in range(n):
    a = int(sys.stdin.readline())
    cnt[a] += 1

j = 1
while j < 10001: 
    if cnt[j] == 0:
        j += 1
    else:
        sys.stdout.write(str(j) + '\n')
        cnt[j] -= 1 # 출력 한 번 하면 개수 감소