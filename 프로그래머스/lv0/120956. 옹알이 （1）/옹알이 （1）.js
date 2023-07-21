function solution(babbling) {
    var answer = 0;
    
    for (let b of babbling) {
        for (let tmp of ["aya", "ye", "woo", "ma"]) {
            b = b.replace(tmp, "0")
        }
    
        if (b.split("").every(i => i === "0")) answer += 1
    }
    
    
    return answer;
}