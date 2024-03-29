# [Silver V] 단어 정렬 - 1181 

[문제 링크](https://www.acmicpc.net/problem/1181) 

### 성능 요약

메모리: 35452 KB, 시간: 108 ms

### 분류

정렬(sorting), 문자열(string)

### 문제 설명

<p>알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.</p>

<ol>
	<li>길이가 짧은 것부터</li>
	<li>길이가 같으면 사전 순으로</li>
</ol>

### 입력 

 <p>첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.</p>

### 출력 

 <p>조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.</p>

### 문제 실패 지점
=> 딕셔너리로 풀어보려다가 시간 오래걸리고 어려워서 포기.
=> for 문 안에 if 문 안에 set 변환(중복 없애기 위해)을 하는 조건식을 썼는데 백준 시간 초과.
=> `.sort(key=len)` 코드를 쓰면 문자열 길이대로 정렬. 또한 sort 가 문자열도 순서에 맞춰서 정렬시켜준다는 사실!
=> `sys.stdin.readline()` 코드에서 개행문자를 지우기 위해서는 `.rstrip()` 이나 `.strip()` 써주기.
