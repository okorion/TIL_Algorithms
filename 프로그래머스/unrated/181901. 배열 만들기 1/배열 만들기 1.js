function solution(n, k) {
    let arr = []
    
    for (let i = 0; i < n; i++) {
        arr.push(i + 1)
    }
    return arr.filter(i => i % k === 0);
}