function solution(arr, flag) {
    var answer = [];
    
    for (let i = 0; i < arr.length; i++) {
        if (flag[i]) {
            for (let k = 0; k < arr[i] * 2; k++) {
                answer.push(arr[i])
            }
        } else {
            answer = answer.slice(0, answer.length - arr[i])
        }
    }
        
    return answer;
}