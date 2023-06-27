function solution(numbers) {
    var answer = 0;
    
    numbers = numbers.sort((b, a) => a - b)
    
    answer = numbers[0] * numbers[1]
    
    return answer;
}