function solution(numbers, k) {
    return (2 * k - 1) % numbers.length === 0 ? numbers.length :parseInt((2 * k - 1) % numbers.length);
}