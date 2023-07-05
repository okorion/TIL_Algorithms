function solution(n) {
    let answer = [];
    
    for (let i = 1; i < n + 1; i++) {
        if (!(n % i)) answer.push(i)
    }
    return answer;
}