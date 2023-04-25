function solution(num_list) {
    var answer = 0;
    
    let a = []
    let b = []
    
    for (let i = 0; i < num_list.length; i++) {
        if (num_list[i] % 2) {
            a.push(num_list[i])
        } else {
            b.push(num_list[i])
        }
    }
    
    console.log(Number(a.join('')) + Number(b.join('')))
    
    answer = Number(a.join('')) + Number(b.join(''))
    
    return answer;
}