function solution(arr) {
    var answer = 1;
    var arrLength = arr.length
    
    for (let i = 0; i < arrLength; i++) {
        for (let j = i; j < arrLength; j++) {
            if (arr[i][j] !== arr[j][i]) answer = 0
        }
    }
    
    return answer;
}