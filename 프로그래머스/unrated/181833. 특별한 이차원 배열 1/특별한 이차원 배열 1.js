function solution(n) {
    var answer = [];
    
    for (let i = 0; i < n; i++) {
        var tmp = [];
        
        for (let j = 0; j < n; j++) {
            tmp.push(0)
        }
        
        tmp[i] = 1
        answer.push(tmp)
    }
    
    return answer;
}