function solution(myString) {
    var answer = '';
    
    for (let str of myString) {
        if (str === "a" || str === "A") {
            answer += "A"
        } else {
            answer += str.toLowerCase()
        }
    }
    
    return answer;
}