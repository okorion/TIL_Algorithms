function solution(myString, pat) {
    var answer = 0;
    myString = myString.toUpperCase()
    pat = pat.toUpperCase()
    
    myString.includes(pat) ? answer = 1 : answer = 0
    
    return answer;
}