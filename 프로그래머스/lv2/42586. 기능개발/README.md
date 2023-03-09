# [level 2] 기능개발 - 42586 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42586) 

### 성능 요약

메모리: 10 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 스택／큐

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.</p>

<p>또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.</p>

<p>먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.</p>

<h5>제한 사항</h5>

<ul>
<li>작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.</li>
<li>작업 진도는 100 미만의 자연수입니다.</li>
<li>작업 속도는 100 이하의 자연수입니다.</li>
<li>배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>progresses</th>
<th>speeds</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[93, 30, 55]</td>
<td>[1, 30, 5]</td>
<td>[2, 1]</td>
</tr>
<tr>
<td>[95, 90, 99, 99, 80, 99]</td>
<td>[1, 1, 1, 1, 1, 1]</td>
<td>[1, 3, 2]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.<br>
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.<br>
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다. </p>

<p>따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.</p>

<p>입출력 예 #2<br>
모든 기능이 하루에 1%씩 작업이 가능하므로, 작업이 끝나기까지 남은 일수는 각각 5일, 10일, 1일, 1일, 20일, 1일입니다. 어떤 기능이 먼저 완성되었더라도 앞에 있는 모든 기능이 완성되지 않으면 배포가 불가능합니다.</p>

<p>따라서 5일째에 1개의 기능, 10일째에 3개의 기능, 20일째에 2개의 기능이 배포됩니다.</p>

<p>※ 공지 - 2020년 7월 14일 테스트케이스가 추가되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges


<br/>
<br/>

### 풀이

 
1) queue FIFO 을 활용한 풀이 (통과)
```
def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
```

progresses = [93,30,55]

speeds = [1,30,5]  

 

1) count, time 변수를 설정해둔다. 

2) 첫번째가 100이 될때까지 loop 를 돌며 time 을 늘린다. 

    else --> time+=1

3) (time =7) 이 되면  첫번째 값이(93) 100이 되어 if에 따라 pop 되고 count +=1

4) 현재 time 이 7이기 때문에 두번째 값(30)도 if에 따라 pop 되고 count +=1 

5) 세번째 값은 100이 안되기 때문에 loop를 돌며 time 을 늘리는데 

    2) 번과 달리 그전에 완성된 친구들 count 값이 있기 때문에 이 친구들을 출시해줘야함 

        따라서 answer 리스트에 append하고 count 초기화!!! 

    그후에 loop를 돌며 time 을 늘리는데 

6) 세번째 값(55)이 100을 넘으면 count +=1 하고 

    이 count 를 다시한번 answer 리스트에 append 해줌으로써 마지막 제품까지 출시 ! 

 

 

 

2) 소요 시간을 미리 계산해두기 math.ceil 을 활용해서 
 
```
import math


def solution(progresses, speeds):
    progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0, 0

    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(progresses) - front)  

    return answer
 ```

 

1) math.ceil 을 활용해서 소요시간을 각각 구한다. 

math.ceil 은 소수점 올림  +)math.floor 내림, round는 반올림 

주어진 조건에서 계산하면 progresses = [7,3,9]

 

 

2)  progresses 의 각 소요시간을 확인하는데 이때 front 에 가장 오래걸린 소요 시간의 인덱스를 저장해둔다. 

우선 초기값으론 0인덱스 

 

3) idx = 0 : 첫번째 수(7) 보다 첫번째 수 (7) 는 같기 때문에 pass ==> front = 0

4) idx = 1 : 첫번째 수(7) 보다 두번째 수(3) 는 작기 때문에 pass ==> front = 0

5) idx = 2 : 첫번째 수(7) 보다 세번째 수(9) 는 크기 때문에 

         - 현재 인덱스부터 프론트인덱스의 차를 구하고 이를 answer에 append (그 전까지 친구들은 동시 출시니까)

         - 프론트인덱스를 현재인덱스로 업데이트! ==> front = 2

---- 반복문 완료 ---

6) 맨 마지막에 현재 프론트인덱스와 전체 길이의 차를 구해서 남은 친구들 다 출시 

 

 
### 정리
1) 모든 풀이 과정을 다 리스트에 담아두는 방식으로 접근하지 x --> 원하는대로 구현이 안되기 쉽상. 

 

2) 입출력 순서에 대한 언급이 있다면, stack , queue 이라 간파하고 pop 으로 풀려고 해보기 

 

stack 의 경우에는 별도의 리스트 만들고 (stack_list)

반복하며 stack_list.pop() 으로 접근하면 쉽게 풀림 ex) () {} 문제들. 

queue 의 경우는 pop(0)

참고링크: https://huidea.tistory.com/15
