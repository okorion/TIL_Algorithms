function solution(myString) {
    var answer = [];
    let cnt = 0;
    
    for (let str of myString.split('')) {
        if (str === 'x') {
            answer.push(cnt)
            cnt = 0
        }
        
        if (str !== 'x') cnt += 1
    }
    
    if (myString.split('')[myString.length - 1] === 'x') answer.push(0)
    if (myString.split('')[myString.length - 1] !== 'x') answer.push(cnt)
    
    return answer;
}