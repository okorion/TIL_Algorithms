function solution(quiz) {
    var ans = [];
    
    for (let q of quiz) {
        let answer = 0
        let arr = q.split(" ")
        
        let num = ""
        let plusMinus = 1
        
        for (let a of arr) {
            if (a === "+") {
                plusMinus = 1
                answer += Number(num)
                num = ""
            }
            else if (a === "-") {
                plusMinus = -1
                answer += Number(num)
                num = ""
            }
            else if (a === "=") {
                answer += plusMinus * Number(num)
                num = ""
            }
            else num += a
        }
    answer === Number(num) ? ans.push("O") : ans.push("X")
    }
    return ans;
}