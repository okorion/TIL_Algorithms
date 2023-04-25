function solution(a, b, c) {
    var answer = 0;
    
    let lst = []
    lst.push(a, b, c)
    let set = new Set(lst)
    
    console.log(lst.length)
    console.log(set.size)
    
    let s = set.size
    
    if (s <= 3) {
        answer += a + b + c
    }
    if (s <= 2) {
        answer *= a ** 2 + b ** 2 + c ** 2
    }
    if (s <= 1) {
        answer *= a ** 3 + b ** 3 + c ** 3
    }
    
    return answer;
}