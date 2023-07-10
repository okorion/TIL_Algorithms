function solution(array) {
    let answer = "";
    let ans = 0;
    
    for (let i = 0; i < array.length; i++) {
        answer += String(array[i])
    }
    
    for (let j = 0; j < answer.length; j++) {
        if (answer[j] === "7") {
            ans += 1
        }
    }
    
    return ans;
}