function solution(number, n, m) {
    var answer = 0;
    
    if (number % n || number % m) {
        answer = 0
    } else {
        answer = 1
    }
    
    return answer;
}