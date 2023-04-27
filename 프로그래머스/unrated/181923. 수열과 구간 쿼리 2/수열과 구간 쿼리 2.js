function solution(arr, queries) {
    var answer = [];
    
    for (let i = 0; i < queries.length; i++) {
        let start = queries[i][0]
        let end = queries[i][1]
        let mid = queries[i][2]
        
        let flag = -1
        let mini = 1000000
        
        for (let k = start; k <= end; k++) {
            // console.log(start, end, mid, k)
            
            if (arr[k] > mid) {
                mini = Math.min(mini, arr[k])
            }
            // console.log(mini)
        }
        
        if (mini === 1000000) {
            answer.push(-1)
        } else {
            answer.push(mini)
        }
    }
    
    return answer;
}