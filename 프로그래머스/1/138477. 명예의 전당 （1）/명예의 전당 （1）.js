function solution(k, score) {
    var answer = [];
    var temp = [];
    
    score.forEach((s) => {
        temp.push(s)
        temp.sort((a, b) => b - a)
        
        if (temp.length <= k) {
            answer.push(temp[temp.length - 1])
        } else {
            answer.push(temp[k - 1])
        }
    })
    
    return answer;
}