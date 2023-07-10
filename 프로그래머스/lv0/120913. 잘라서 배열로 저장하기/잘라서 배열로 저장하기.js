function solution(my_str, n) {
    var answer = [];
    
    for (let i = 0; i < Math.ceil(my_str.length / n); i++) {  // 수정: 올림 함수(Math.ceil) 사용하여 반복 횟수 계산
        answer.push(my_str.slice(i * n, i * n + n));  // 수정: splice 대신 slice 사용하여 부분 문자열 추출
    }
    
    return answer;
}