function solution(n) {
    var answer = 0;
    
    tmp_array = [...String(n)].map((item) => Number(item))
    
    for (let tmp of tmp_array) answer += tmp
    
    return answer;
}