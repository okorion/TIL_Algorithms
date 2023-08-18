function solution(a, b) {
    var answer = 0;
    
    if (a % 2 && b % 2) answer = a**2 + b**2
    else if (a % 2 || b % 2) answer = 2 * (a + b)
    else if (!(a % 2) && !(b % 2)) answer = (a - b > 0) ? a - b : b - a
    
    return answer;
}