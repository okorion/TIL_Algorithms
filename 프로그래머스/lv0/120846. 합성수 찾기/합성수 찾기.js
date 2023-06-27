function solution(n) {
    var answer = 0;
    
    for (let i = 1; i < n + 1; i++) {
        let num = 0
        for (let j = 1; j < i + 1; j++) {
            if (i / j === parseInt(i / j)) num += 1
        }
        
        if (num >= 3) {
            answer += 1
        }
    }
    
    return answer;
}