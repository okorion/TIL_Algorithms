function solution(my_string) {
    const answer = new Array(52).fill(0);
    
    for (const char of my_string) {
        const charCode = char.charCodeAt();
        
        if (charCode >= 65 && charCode <= 90) { // 대문자인 경우
            answer[charCode - 65] += 1;
        } else if (charCode >= 97 && charCode <= 122) { // 소문자인 경우
            answer[charCode - 71] += 1;
        }
    }
    
    return answer;
}
