function solution(strArr) {
    var answer = [];
    
    for (let str of strArr) {
        !str.includes("ad") && answer.push(str)
    }
    
    return answer;
}