function solution(n) {
    let answer = 0
    parseInt(Math.sqrt(n)) === Math.sqrt(n) ? answer = 1 : answer = 2
    
    return answer
}