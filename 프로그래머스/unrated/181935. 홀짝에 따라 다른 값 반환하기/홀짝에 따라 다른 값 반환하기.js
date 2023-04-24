function solution(n) {
    var answer = 0;
    
    if (n % 2) {
        for (let i = 1; i * 2 - 1 <= n; i++) {
            answer += i * 2 - 1
            console.log(i * 2 - 1)            
        }
    } else {
        for (let i = 1; i * 2 <= n; i++) {
            answer += (i * 2) ** 2
        }
    }
    
    return answer;
}