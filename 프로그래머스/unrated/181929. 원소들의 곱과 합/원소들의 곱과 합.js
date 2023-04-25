function solution(num_list) {
    var answer = 0;
    
    let a = num_list.reduce((a, b) => a + b, 0)
    let b = 1
    
    for (let i = 0; i < num_list.length; i++) {
        b *= num_list[i]
    }
    
    if ( b < a ** 2) {
        return 1
    } else {
        return answer
    }
}