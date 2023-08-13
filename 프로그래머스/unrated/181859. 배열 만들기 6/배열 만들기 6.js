function solution(arr) {
    var answer = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (answer.length === 0) {
            answer.push(arr[i])
        }
        
        else if (answer[answer.length - 1] === arr[i]) {
            answer = answer.slice(0, answer.length - 1)
        }
        
        else if (answer[answer.length - 1] !== arr[i]) {
            answer.push(arr[i])
        }
    }
    
    
    return answer.length === 0 ? [-1] : answer;
}