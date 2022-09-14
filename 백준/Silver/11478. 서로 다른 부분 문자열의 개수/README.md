# [Silver III] 서로 다른 부분 문자열의 개수 - 11478 

[문제 링크](https://www.acmicpc.net/problem/11478) 

### 성능 요약

메모리: 252428 KB, 시간: 1436 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.</p>

<p>부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.</p>

<p>예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.</p>

### 입력 

 <p>첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.</p>

### 출력 

 <p>첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.</p>

### 문제풀이 실패 지점

=> stdin.readline이 input보다 빠른 입출력 형식

=> 이 문제에서sys 라이브러리를 이용하였을 때 틀린 답이 출력되는 이유는 stdin.readline이 개행문자까지 입력받는 입력 형식이기 때문

=> input을 사용하여 입력을 받으면 S는'ababc'가 되어 len(S)는 5가 되지만, stdin.readline을 사용하여 입력을 받으면 S는'ababc\n'이 되어 len(S)는 7이 됨.
