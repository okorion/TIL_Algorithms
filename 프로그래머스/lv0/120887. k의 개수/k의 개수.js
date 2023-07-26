function solution(i, j, k) {
    var answer = 0;
    
    for (let x = i; x < j + 1; x++) {
        let tmp = String(x).split("")
        
        for (let t of tmp) {
            if (t == k) answer += 1
        }
    }
    
    return answer;
}