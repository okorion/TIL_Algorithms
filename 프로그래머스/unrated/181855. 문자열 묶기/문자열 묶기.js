function solution(strArr) {
    var answer = 0;
    var lengthObject = {};
    
    for (let i = 0; i < strArr.length; i++) {
        if (!lengthObject.hasOwnProperty(strArr[i].length)) {
            lengthObject[strArr[i].length] = 0
        }
        
        lengthObject[strArr[i].length] += 1
    }
    
    let values = Object.values(lengthObject)
    
    for (let v of values) {
        if (v > answer) {
            answer = v
        }
    }
    
    return answer;
}