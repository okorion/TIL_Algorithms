function solution(my_string) {
    var answer = 0;
    
    const numList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for (let i = 0; i < my_string.length; i++) {
        if (numList.includes(my_string[i])) {
            answer += Number(my_string[i])
        }
    }
    
    return answer;
}