function solution(slice, n) {
    for (let i = 1; i < n + 1; i++) {
        if (slice * i >= n) {
            return i
        }
    }
}