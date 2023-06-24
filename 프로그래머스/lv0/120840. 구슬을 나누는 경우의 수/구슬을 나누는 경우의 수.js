function solution(balls, share) {
    var answer = 1;
    
    for (let i = balls; i > balls - share; i--) {
        answer *= i
    }
    
    for (let i = share; i > 0; i--) {
        answer /= i
    }
    
    return parseInt(answer);
}