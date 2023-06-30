function solution(s) {
    var answer = 0;
    let tmpList = [];
    
    
    s.split(" ").map((item) => {
        if (Number(item) || item === "0") tmpList.push(Number(item));
        else tmpList.pop();
    })
    
    answer = tmpList.reduce((a, b) => a + b, 0)
    return answer;
}