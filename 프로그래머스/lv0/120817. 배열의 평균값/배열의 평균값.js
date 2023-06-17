function solution(numbers) {
    const sum = numbers.reduce((acc, number) => acc + number, 0)
    
    return sum / numbers.length
}