function solution(num_list) {
    let answer = 0;
    
    for (let n of num_list) { // Use "of" instead of "in" to iterate over array elements
        let tmp = 0;
        
        while (n > 1) {
            if (n % 2 === 0) {
                n /= 2;
                tmp += 1;
            } else {
                n = (n - 1) / 2;
                tmp += 1; // One subtraction and one division
            }
        }
        
        answer += tmp;
    }
    
    return answer;
}

