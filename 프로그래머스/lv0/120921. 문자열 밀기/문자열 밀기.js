function solution(A, B) {
    var answer = 0;
    let AA = A + A
    
    function rotate(a) {
        const tmpA = a.split("")[a.length - 1] + a.split("").splice(0, a.length - 1).join("")
        
        return tmpA
    }
    
    for (let i = 0; i < A.length; i++) {
        if (A === B) return i
        A = rotate(A)
    }
    
    return -1
}