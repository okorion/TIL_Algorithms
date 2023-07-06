function solution(array) {
    let answer = [];
    
    let maxNum = Math.max(...array)
    let maxIdx = array.findIndex(num => num === maxNum)
    
    answer.push(maxNum)
    answer.push(maxIdx)
    
    return answer;
}