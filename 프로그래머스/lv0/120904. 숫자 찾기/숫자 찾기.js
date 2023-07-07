function solution(num, k) {
    var answer = 0;
    
    str_num = [...String(num)]
    
    for (let i = 0; i < str_num.length; i++) {
        if (str_num[i] === String(k)) {
            return i + 1
        }
        if (i === str_num.length - 1) return -1
    }
}