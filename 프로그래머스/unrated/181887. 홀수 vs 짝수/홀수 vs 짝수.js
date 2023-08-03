function solution(num_list) {
    var answer = 0;
    let left = 0;
    let right = 0;
    
    for (let i = 0; i < num_list.length; i++) {
        (i % 2) ? left += num_list[i] : right += num_list[i]
    }
    
    if (left >= right) {
        answer = left
    } else {
        answer = right
    }
    
    return answer;
}