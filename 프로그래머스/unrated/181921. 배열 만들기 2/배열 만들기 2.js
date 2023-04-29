function solution(l, r) {
    var answer = [];
    
    for (let i = l; i <= r; i++) {
        n = i.toString()
        n_2 = new Set(n)
        // console.log(n_2)
        
        if (JSON.stringify(Array.from(n_2)) === JSON.stringify(['0']) ||
            JSON.stringify(Array.from(n_2)) === JSON.stringify(['0', '5']) ||
            JSON.stringify(Array.from(n_2)) === JSON.stringify(['5', '0']) ||
            JSON.stringify(Array.from(n_2)) === JSON.stringify(['5'])) {
            answer.push(i);
        }
    }
    
    if (answer.length > 0) {
        return answer
    } else {
        return [-1]
    }
}