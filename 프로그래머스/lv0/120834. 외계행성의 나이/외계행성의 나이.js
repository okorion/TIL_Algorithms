function solution(age) {
    var answer = '';
    let array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    
    age = age.toString()
    
    for (let j = 0; j < Number(age); j++) {
        for (let i = 0; i < 10; i++) {
            if (Number(age[j]) === i) {
                answer += array[i]
                
                console.log('23523')
            }
        }
    }
    
    return answer;
}