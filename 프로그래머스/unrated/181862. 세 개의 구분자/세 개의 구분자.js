function solution(myStr) {
    var answer = [];
    var tmp = "";
    
    for (let i = 0; i < myStr.length; i++) {
        if (myStr[i] === "a" || myStr[i] === "b" || myStr[i] == "c") {
            (tmp !== "") && answer.push(tmp)
            tmp = ""
        } else {
            tmp += myStr[i]
        }
        
        if ((tmp !== "") && (i === myStr.length - 1)) answer.push(tmp)
    }
    
    if (answer.length === 0) return ["EMPTY"]
    
    return answer;
}