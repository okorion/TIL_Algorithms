function isPowerOfTwo(num) {
    return (num > 0) && ((num & (num - 1)) === 0);
}

function solution(arr) {
    var answer = [];
    
    answer = [...arr]
    
    while (true) {
        if (!isPowerOfTwo(answer.length)) {
        answer.push(0)
        } else {
            break;
        }
    }
    
    return answer;
}