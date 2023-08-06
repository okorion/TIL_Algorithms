function solution(arr) {
    let answer = 0;
    
    while (true) {
        let transformed = [...arr];
        
        for (let i = 0; i < transformed.length; i++) {
            if (transformed[i] >= 50 && transformed[i] % 2 === 0) {
                transformed[i] /= 2;
            } else if (transformed[i] < 50 && transformed[i] % 2 === 1) {
                transformed[i] = transformed[i] * 2 + 1;
            }
        }
        
        if (JSON.stringify(transformed) === JSON.stringify(arr)) {
            break;
        }
        
        arr = transformed;
        answer++;
    }
    
    return answer;
}