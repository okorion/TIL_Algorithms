function solution(numbers, direction) {
    var answer = [];
    
    if (direction === "right") {
        answer = [numbers[numbers.length - 1], ...numbers.splice(0, numbers.length - 1)]
    } else {
        answer = [...numbers.slice(1), numbers[0]]
    }
    
    return answer;
}