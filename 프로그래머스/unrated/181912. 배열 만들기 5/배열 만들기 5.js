function solution(intStrs, k, s, l) {
    var answer = [];
    
    for (let i = 0; i < intStrs.length; i++) {
        num = intStrs[i].substring(s, s + l)
        
        if (num > k) {
            answer.push(Number(num))
        }
    }
    
    return answer;
}