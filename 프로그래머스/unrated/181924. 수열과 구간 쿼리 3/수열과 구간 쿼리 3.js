function solution(arr, queries) {
    var answer = [];
    
    for (i = 0; i < queries.length; i++) {
        let a = queries[i][0]
        let b = queries[i][1]
        let tmp = 0
        
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
    }
    
    return arr;
}