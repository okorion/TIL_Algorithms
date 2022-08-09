# [Silver IV] 숫자 카드 2 - 10816 

[문제 링크](https://www.acmicpc.net/problem/10816) 

### 성능 요약

메모리: 128220 KB, 시간: 800 ms

### 분류

이분 탐색(binary_search), 자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 정렬(sorting)

문제풀이 실패 지점
=> (1시간 소요) 이진탐색으로 풀었는데 시간초과 => for 문으로 풀었는데 시간초과 => 구글링을 통해 해쉬맵을 이용하거나 collections의 Counter를 사용하는 방법 중 후자 선택
=> Counter 함수를 통해 딕셔너리 형태로 바꾼 뒤에 조건문을 설정하여 정답 출력
