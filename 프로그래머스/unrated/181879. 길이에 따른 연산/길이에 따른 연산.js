function solution(num_list) {
    var answer = 0;
    
    answer = num_list.length >= 11 ? num_list.reduce((a, b) => a + b) : num_list.reduce((a, b) => a * b)
    
    return answer;
}