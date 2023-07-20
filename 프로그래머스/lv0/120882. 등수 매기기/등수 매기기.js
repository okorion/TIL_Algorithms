function solution(score) {
    var answer = [];
    let result = [];
    
    for (let s of score) {
        answer.push(arr(s))
    }
    console.log(answer)
    ans = [...answer].sort((a, b) => b - a)
    console.log(ans)
    
    for (let a of answer) {
        result.push([...ans].indexOf(a) + 1)
    }
    
    return result;
}

function arr(list) {
    let a = list[0]
    let b = list[1]
    
    return (a + b) / 2
}