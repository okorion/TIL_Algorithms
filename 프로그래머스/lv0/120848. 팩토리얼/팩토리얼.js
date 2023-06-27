function solution(n) {
    var answer = 1;
    let num = 1;
    
    while (answer <= n) {
        answer *= num
        num ++
    }
    
    return (num - 2);
}