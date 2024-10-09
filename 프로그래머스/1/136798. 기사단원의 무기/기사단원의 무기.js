function calculateDivisors(number) {
    const divisors = Array(number + 1).fill(0);

    // 에라토스테네스의 체를 사용하여 약수 개수 계산
    for (let i = 1; i <= number; i++) {
        for (let j = i; j <= number; j += i) {
            divisors[j]++;
        }
    }
    return divisors;
}

function solution(number, limit, power) {
    let answer = 0;

    const divisors = calculateDivisors(number);

    for (let i = 1; i <= number; i++) {
        let count = divisors[i];
        if (count > limit) {
            count = power;
        }
        answer += count;
    }

    return answer;
}
