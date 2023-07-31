function solution(arr) {
    var answer = [];
    let tmp = [];
    
    if (!arr.some(i => i === 2)) return [-1]
    
    for (let a of arr) { // for...of 루프를 사용하여 배열의 값을 얻어옴
        console.log(a)
        if (a === 2) {
            if (answer.length === 0) {
                answer.push(2)
                tmp = [];
            } else {
                answer.push(...tmp);
                answer.push(2);
                tmp = [];
            }
        } else {
            tmp.push(a); // tmp 배열에 2가 아닌 값을 추가
        }
    }
    
    return answer;
}
