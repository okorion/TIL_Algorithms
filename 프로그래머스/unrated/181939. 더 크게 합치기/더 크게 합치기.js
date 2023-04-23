function solution(a, b) {
    a = String(a)
    b = String(b)
    
    return Math.max(Number(a + b), Number(b + a))
}