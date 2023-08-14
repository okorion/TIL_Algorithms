function solution(arr, k) {
    const uniqueNumbers = new Set(arr);
    const answer = [...uniqueNumbers].slice(0, k);

    while (answer.length < k) {
        answer.push(-1);
    }

    return answer;
}
