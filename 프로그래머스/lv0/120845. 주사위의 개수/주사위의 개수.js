function solution(box, n) {
    var answer = 1;
    
    box.map((i) => answer *= parseInt(i/n))
    
    return answer;
}