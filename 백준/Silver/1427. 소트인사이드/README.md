# [Silver V] 소트인사이드 - 1427 

[문제 링크](https://www.acmicpc.net/problem/1427) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

정렬(sorting), 문자열(string)

### 문제 설명

<p>배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.</p>

### 입력 

 <p>첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.</p>

### 문제풀이 실패 지점

 입력을 받아올 때 `sys.stdin.readline' 을 사용하고 있었는데 이번 문제에서 *런타임 에러 (ValueError)*가 계속 나서 게시판 확인하여 input으로 고쳐서 다시 코딩함.  
=> sys.stdin.readline()은 한줄 단위로 입력받기 때문에, 개행문자가 같이 입력 받아짐.  
=> 만약 3을 입력했다면, 3\n 이 저장되기 때문에, 개행문자를 제거해야 함. 또한, 변수 타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 함.  
</br>
참고링크: [[Python 문법] 파이썬 입력 받기(sys.stdin.readline)](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
