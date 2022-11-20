## 문제01 (boj. 1110)

[백준) 더하기 사이클](https://www.acmicpc.net/problem/1110)

- line 07 : ‘더하기 사이클’ 과정 자체를 함수로 만들었습니다.
- line 08 : 이때, 맨 오른쪽에 위치한 숫자를 `lnum` 로 저장하고 이후 반복문을 수행합니다.
- line 09 - 10 : `%10` 연산과 `//10` 연산을 사용해서 각 자릿수 별로 숫자를 남기고자했습니다.
- line 15: 최종 더하기 사이클의 결과가 만약 맨 처음 `n` 과 같다면 그 즉시 프로그램이 종료합니다.
- line 16 : 최종 더하기 사이클의 결과가 만약 맨 처음 `n` 과 같지 않다면 사이클 횟수를 1증가시켜주고 다시 더하기 사이클을 재귀적으로 수행합니다.

<br>

---

## 문제02 (boj. 9095)

[백준) 1, 2, 3 더하기](https://www.acmicpc.net/problem/9095)

- line 05 : 입력의 최대 숫자가 11이므로 인덱스값 11이 최대인 12크기의 배열을 만들었습니다.
- line 06 : 이후 뒷부분의 dp 과정에서 `n-1`, `n-2`, `n-3`항의 값이 필요하기 떄문에 처음 초기값인 dp[0], dp[1], dp[2]는 직접 값을 넣어주었습니다.
- line 08 : 반복문을 돌면서 dp 테이블을 채워줍니다.
- line 11 : 이후 입력 숫자에 따라 값을 출력합니다.

<br>

- dp 테이블을 채우는 규칙은 합을 나타내는 숫자가 1, 2, 3밖에 없다는 점을 이용했습니다.

```
dp[n] += dp[n - 1] # dp[n - 1]의 값들에 1을 더한 결과
dp[n] += dp[n - 2] # dp[n - 2]의 값들에 2을 더한 결과
dp[n] += dp[n - 3] # dp[n - 3]의 값들에 3을 더한 결과

```

<br>

---

## 문제03 (boj. 1182)

[백준) 부분수열의 합](https://www.acmicpc.net/problem/1182)

- 파이썬 외부 모듈인 `itertools.combinations()`를 사용해서 수열들의 전체 조합을 구했습니다.

<br>

- line 09 : 조합의 원소 개수를 1부터 n까지의 모든 경우의 수를 추출했습니다.
- line 11 : 이후 각 원소 개수별로 추출한 조합의 값으로 전부 반복문을 돌려, 모든 경우에 수에 대한 합을 구했습니다.
- line 12 : 이때 이러한 합이 입력으로 주어진 `s`와 같다면 answer의 값을 1 증가시켜주었습니다.