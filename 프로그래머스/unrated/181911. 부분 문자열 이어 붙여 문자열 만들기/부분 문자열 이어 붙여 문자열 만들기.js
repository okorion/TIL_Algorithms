function solution(my_strings, parts) {
    var answer = '';
    
    for (let i = 0; i < parts.length; i++) {
        let start = parts[i][0]
        let end = parts[i][1]
        
        answer += my_strings[i].substring(start, end + 1)
    }
    
    return answer;
}