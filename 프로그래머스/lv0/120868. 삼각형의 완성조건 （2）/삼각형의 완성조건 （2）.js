function solution(sides) {
    let answer = 0

    for (let i = 1; i < sides.reduce((a, b) => a + b) + 1; i++) {
        let max_num = Math.max(...sides, i)
        
        if (max_num < [...sides, i].reduce((a, b) => a + b) - max_num) answer += 1
    }
        
    return answer;
}