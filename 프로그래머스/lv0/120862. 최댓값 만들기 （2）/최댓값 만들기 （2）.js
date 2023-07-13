function solution(numbers) {
    var answer = 0;
    
    let a = [...numbers].sort((x, y) => x - y)
    console.log(a)
    let b = [...numbers].sort((x, y) => x - y).reverse()
    console.log(a, b)
    return a[0] * a[1] > b[0] * b[1] ? a[0] * a[1] : b[0] * b[1];
}