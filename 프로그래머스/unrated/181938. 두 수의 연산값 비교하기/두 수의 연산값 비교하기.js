function solution(a, b) {
    console.log(typeof(a))
    res = Math.max(Number(String(a) + String(b)), 2 * a * b)
    return res;
}