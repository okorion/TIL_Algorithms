function solution(my_string, indices) {
    var answer = '';
    let arr = my_string.split("")
    let table = new Array(arr.length).fill(0)
    
    for (let i of indices) {
        table[i] += 1
    }
    
    for (let i = 0; i < arr.length; i++) {
        if (table[i] === 0) answer += arr[i]
    }
    
    return answer;
}