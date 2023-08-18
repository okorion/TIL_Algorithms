function solution(picture, k) {
    var answer = [];
    
    for (let p of picture) {
        let tmp = p.split("")
        let str = ""
        
        for (let t of tmp) {
            for (let i = 0; i < k; i++) {
                str += t
            }
        }
        for (let i = 0; i < k; i++) {
            answer.push(str)
        }
    }
    
    return answer;
}