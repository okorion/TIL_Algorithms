function solution(strArr) {
    var answer = [];
    
    strArr.map((i, idx) => !(idx % 2) ? answer.push(i.toLowerCase()) : answer.push(i.toUpperCase()))
    
    return answer;
}