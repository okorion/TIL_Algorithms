function solution(num_list, n) {
    let left = num_list.slice(n, num_list.length)
    let right = num_list.slice(0, n)

    return left.concat(right)
}