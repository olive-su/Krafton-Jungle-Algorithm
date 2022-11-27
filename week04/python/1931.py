import sys

input = sys.stdin.readline
n = int(input())
meeting, cnt = [], 1

for _ in range(n):
    meeting.append(tuple(map(int, input().split())))

meeting.sort(key=lambda x : x[0]) # 회의가 먼저 시작하는 거 정렬
meeting.sort(key=lambda x : x[1]) # 회의가 먼저 끝나는 거 정렬

now = meeting[0][1]

for m in range(1, n):
    if meeting[m][0] >= now:
        now = meeting[m][1]
        cnt += 1

print(cnt)
