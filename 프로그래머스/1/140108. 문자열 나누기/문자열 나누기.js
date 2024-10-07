function solution(s) {
    var answer = 0;
    
    let x = 0;
    let notx = 0;
    
    let flag = s[0];
    
    s.split('').forEach((e, index) => {
        if (e === flag) {
            x += 1
        } else {
            notx += 1
        }
        
        if (x === notx) {
            x = 0;
            notx = 0;
            answer += 1
            console.log('flag', flag)
            flag = s[index + 1]          
        } else {
            if (s.length === index + 1) {
                answer += 1
            }
        }
    })
    
    return answer;
}