function solution(n) {
    var answer = [];
    
    for (let i = 2; i < n + 1; i++) {
        
        while (n % i === 0) {
            n /= i;
            if (!answer.includes(i)) answer.push(i);
        } 
    }
    
    return answer.sort((a, b) => a - b);
}