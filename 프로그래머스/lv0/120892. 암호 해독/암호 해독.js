function solution(cipher, code) {
    var answer = '';
    
    if (cipher.length === 1) {
        if (code === 1) {
            return cipher[0]
        }
    }
    
    for (let i = 1; i < cipher.length + 1; i++) {
        if (i * code - 1 < cipher.length) {
            answer += cipher[i * code - 1]
        }
    }
    return answer;
}