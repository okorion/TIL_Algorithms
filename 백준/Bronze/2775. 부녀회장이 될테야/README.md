# [Bronze I] 부녀회장이 될테야 - 2775 

[문제 링크](https://www.acmicpc.net/problem/2775) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

구현(implementation), 수학(math)


### 문제풀이 실패 지점

 마지막 코드로 `print(int(temp))` 를 썼었는데 792 * ( 13/6 ) = 1715.9999998로 계산된 이후 1715 라는 값이 출력되어 실패했음. (정답은 1716)
 반올림하는 코드인 `print(round(temp))`를 써서 통과함.
 
 => 참고링크 - https://wikidocs.net/106676 "020 분수를 정확하게 계산하려면? = fractions"
 
