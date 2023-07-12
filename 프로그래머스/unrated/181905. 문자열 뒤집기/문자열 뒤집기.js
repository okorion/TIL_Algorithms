function solution(my_string, s, e) {
    var answer = '';
    
    answer += my_string.split("").splice(0, s).join("")
    
    answer += my_string.split("").splice(s, e - s + 1).reverse().join("")
    
    answer += my_string.split("").splice(e + 1, my_string.length - e).join("")
    
    return answer;
}