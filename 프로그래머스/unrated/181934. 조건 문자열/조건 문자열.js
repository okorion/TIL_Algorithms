function solution(ineq, eq, n, m) {
    var answer = 0;
    let flag = true;
    
    if (ineq === "<" && eq === "=") {
        if (n > m) {
            flag = false
        }
    } else if (ineq === "<" && eq === "!") {
        if (n >= m) {
            flag = false
        }
        
    } else if (ineq === ">" && eq === "=") {
        if (n < m) {
            flag = false
        }
    } else if (ineq === ">" && eq === "!") {
        if (n <= m) {
            flag = false
        }
    }
    
    answer = Number(flag)
    
    return answer;
}