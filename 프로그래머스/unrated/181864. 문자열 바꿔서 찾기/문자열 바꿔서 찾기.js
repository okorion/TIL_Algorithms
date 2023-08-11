function solution(myString, pat) {
    var answer = 0;
    myString = myString.replaceAll('A', 'b')
    myString = myString.replaceAll('B', 'a')
    
    myString = myString.toUpperCase()
    
    myString.includes(pat) && (answer = 1)
    
    return answer;
}