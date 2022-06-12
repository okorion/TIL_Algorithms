# [Silver III] 소수 구하기 - 1929 

[문제 링크](https://www.acmicpc.net/problem/1929) 

### 성능 요약

메모리: 131584 KB, 시간: 388 ms

### 분류

수학(math), 정수론(number_theory), 소수 판정(primality_test), 에라토스테네스의 체(sieve)

### 문제 설명

<p>M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.</p>

### 출력 

 <p>한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.</p>

### 문제풀이 실패 지점

```cnt = 0
result_list = []

for _ in range(M, N+1, 2):
    for x in range(1, _+1, 2):
        if _ % x == 0:
            cnt += 1

    if cnt == 2:
        result_list.append(_)
    cnt = 0

for __ in result_list:
    print(__)
```

=> for 문 안에 다 넣어서 계산하니 시간 초과 걸려서 그냥 문제에 쓰여진 범위 1,000,000 내에서 소수인 수들 테이블을 따로 만들었음.
=> 구글링에서찾은 팁으로는 range 범위에서 소수 판별하기 위해서는 `N+1`까지 안해도 되고 `N**0.5+1`까지 구하면 된다고 함.
