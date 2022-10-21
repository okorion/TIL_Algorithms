# Python

## TIL Algorithms

</details> 
<details><summary>알고리즘 팁</summary>

#### input과 sys.stdin.readline의 차이점

=> `input()` 내장 함수는 prompt message를 출력하고 개행 문자를 삭제한 값을 리턴.

=> `sys.stdin.readline()` sys 함수는 prompt message를 출력하지 않고 개행 문자를 그대로 리턴. 

=> 개행 문자 리턴으로 인해 백준 문제풀이에서 종종 실패하는 경우가 있기 때문에 `.strip()` 붙여주기 
 
 
#### Prompt Message란?

>  *Prompt*는 컴퓨터가 입력을 기다리고 있음을 가리키기 위해 화면에 나타나는 표시이다. 예를 들어 "직원 이름을 입력하시오"와 같은 메시지도 프롬프트가 될수 있으며, 명령어 중심의 시스템에서는 명령어를 받아들이기 위한 준비가 되었을 때, 미리 정해진 부호를 나타낸다.
>
>  이를테면, dBASE 에서는 점(.)을, [유닉스](http://www.terms.co.kr/UNIX.htm)에서는 $ 또는 %를, [DOS](http://www.terms.co.kr/DOS.htm)에서는 C:\> 등을 표시하는데, 이는 각 시스템별로 특색 있는 프롬프트의 예이다.

```
>>> number = input("숫자를 입력하세요: ")  #input 안의 변수가 prompt message
숫자를 입력하세요: 7
>>> print(number)
7
```
 
</details>

* 이진탐색
* 백트래킹
* DFS
* BFS
* DP
> 14501 퇴사: 뒤에서부터 가능한 비용을 누적하여 max값 비교.

* 구간합
>  `list[i:j]`와 같은 슬라이싱보다 `sum[j] - sum[i-1]` 누적합을 연산하는 방식을 사용하는 것이 성능에 유리. (전자는 시간복잡도 O(N\*2) 후자는 2\*O(N)

<br>

# C / C++

## 알고리즘 문제 풀이

```
#include <stdio.h>        #include <iostream>은 C++

int main(void) {
    int a;
    
    scanf("%d", &a);
    
    printf("%d", a);
}
```

=> `123` 입력 시 `123` 출력

<br>

# JAVA

## 알고리즘 문제 풀이

```
import java.util.*;                  #java.util.Scanner;

public class Main {                  #SWEA에서는 `public class Solution`
    public static void main(String args[]) {            #(String[] args)도 가능!
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        
        System.out.print(a);
    }
}
```

=> `123` 입력 시 `123` 출력
<br>
