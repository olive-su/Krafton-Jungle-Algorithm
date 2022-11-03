n = int(input())

ans = 0
row = [-1] * n

# row[x] (x행)에 퀸을 놓는 경우 유효성 검사
def backtracking(x):
    # 이전 행을 돌면서 놓인 퀸 위치 중 같은 행 또는 열, 대각선이 있는 지 검사
    # 이전 행을 검사하는 이유? - 이전 행은 이미 유효한 위치이기 때문
    for i in range(x):  
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): # 같은 col, 대각선 검사
            return False
    return True

def n_queens(x):
    global ans
    if x == n: # n개의 퀸을 모두 놓았을 경우 ans++
        ans += 1
    else:
        for i in range(n): # row check (열 순회)
            row[x] = i
            if backtracking(x): # 유효하면 다음 스텝으로 넘어감
                n_queens(x+1) # 다른 row 검사(행 순회)
n_queens(0)
print(ans)