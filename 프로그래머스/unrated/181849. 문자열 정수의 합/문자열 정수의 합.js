function solution(num_str) {
    var answer = 0;
    
    for (let str of num_str) {
        answer += Number(str)
    }
    
    return answer;
}