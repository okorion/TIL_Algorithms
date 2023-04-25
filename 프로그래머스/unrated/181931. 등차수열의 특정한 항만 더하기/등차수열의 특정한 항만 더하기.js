function solution(a, d, included) {
    var answer = 0;
    
    let lst = []
    
    for (let i = 0; i < included.length; i++) {
        lst.push((i + a) + (i * (d - 1)))
    }
    console.log(lst)
    
    for (let k = 0; k < included.length; k++) {
        if (included[k] === true) {
            console.log(k)
            answer += lst[k]
        }
    }
    
    return answer;
}