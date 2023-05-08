function solution(my_string, n) {
    var answer = '';
    
    for (let i = 0; i < n; i++) {
        answer += my_string[i + my_string.length - n]
    }
    
    return answer;
}