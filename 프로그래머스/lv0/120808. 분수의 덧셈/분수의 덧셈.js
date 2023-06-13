function Greatest(a, b) {
    if (b === 0) {
        return a
    }
    
    return Greatest(b, a % b)
}

function solution(numer1, denom1, numer2, denom2) {
    var answer = [];
    
    let child = numer1 * denom2 + numer2 * denom1
    let parent = denom1 * denom2
    
    let greatest = Greatest(child, parent)
    
    answer.push(child / greatest)
    answer.push(parent / greatest)
    
    return answer;
}