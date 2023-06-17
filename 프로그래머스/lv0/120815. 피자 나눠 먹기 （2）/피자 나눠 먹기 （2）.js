function solution(n) {
    var answer = 0;
    
    if (n === 1) return 1
    
    for (let i = 1; i < n + 1; i++) {
        if (i * 6 % n === 0) {
            return i
        } else if (i === n) {
            return i * n / n
        }
    }
}