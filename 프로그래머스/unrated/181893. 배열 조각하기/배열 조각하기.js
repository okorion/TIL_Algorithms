function solution(arr, query) {
    var answer = [];
    
    for (let i = 0; i < query.length; i++) {
        if (i % 2) {
            arr = arr.slice(query[i], arr.length)
        } else {
            arr = arr.slice(0, query[i] + 1)
        }
        console.log(arr)
    }
    
    return arr;
}