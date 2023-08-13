function solution(arr) {
    var answer = [];
    
    for (let a of arr) {
        for (let i = 0; i < a; i++) {
            answer.push(a)
        }
        
    }
    
    return answer;
}