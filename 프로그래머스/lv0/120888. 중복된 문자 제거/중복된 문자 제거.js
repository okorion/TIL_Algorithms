function solution(my_string) {
    var answer = '';
    let tempStringList = [];
    
    for (let i = 0; i < my_string.length; i++) {
        if (!tempStringList.includes(my_string[i])) {
            answer += my_string[i]
            tempStringList.push(my_string[i])
        }
    }
    
    return answer;
}