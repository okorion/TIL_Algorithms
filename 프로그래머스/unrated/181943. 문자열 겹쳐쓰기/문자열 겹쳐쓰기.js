function solution(my_string, overwrite_string, s) {
    var answer = '';
    
    for (let i = 0; i < s; i++) {
        answer += my_string[i]
    }
    
    answer += overwrite_string
    
    if (overwrite_string.length + s < my_string.length) {
        let tmp = my_string.length - (overwrite_string.length + s)
        
        for (let i = my_string.length - tmp; i < my_string.length; i++) {
            answer += my_string[i]
        }
    }    
    
    return answer;
}