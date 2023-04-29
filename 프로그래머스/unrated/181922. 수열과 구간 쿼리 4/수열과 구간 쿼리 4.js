function solution(arr, queries) {    
    for (let i = 0; i < queries.length; i++) {
        a = queries[i][0]
        b = queries[i][1]
        c = queries[i][2]
        
        for (let j = a; j <= b; j++) {
            // console.log(arr[j], c, queries[i])
            if (j % c === 0) {
                arr[j] += 1
            }
        }
        // console.log(arr)
    }
    
    return arr;
}