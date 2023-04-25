function solution(code) {
    var answer = '';
    
    let mode = false
    
    for (let i = 0; i < code.length; i++) {
        if (code[i] === "1") {
            mode = !mode
        } else if (i % 2) {
            if (mode === false) {
            } else {
                answer += code[i]
            }
        } else {
            if (mode === true) {
            } else {
                answer += code[i]
            }            
        }
    }
    
    if (answer) {
        return answer
    } else {
        return "EMPTY"
    }
}