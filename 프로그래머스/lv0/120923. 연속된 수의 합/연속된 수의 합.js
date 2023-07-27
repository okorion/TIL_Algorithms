function solution(num, total) {
    var answer = [];
    let start = 0;
    let v = 0;
    
    for (let i = 0; i < num; i++) v += i
    
    start = (total - v) / num
    
    for (let k = start; k < start + num; k++) answer.push(k)
    
    return answer;
}