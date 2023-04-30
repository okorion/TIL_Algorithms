function solution(n) {
    var answer = [];
    
    while (n >= 1) {
        answer.push(n)
        
        if (n === 1) {
            break
        } else if (n % 2) {
            n = 3 * n + 1
        } else {
            n /= 2
        }
    }
    return answer;
}