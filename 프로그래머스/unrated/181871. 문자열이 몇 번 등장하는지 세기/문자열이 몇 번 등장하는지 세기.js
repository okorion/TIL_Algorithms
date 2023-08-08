function solution(myString, pat) {
    var answer = 0;
    
    for (let i = 0; i < myString.length - pat.length + 1; i++) {
        if (myString.split("").splice(i, pat.length).join("") === pat.split("").join("")) answer += 1
    }
    return answer;
}