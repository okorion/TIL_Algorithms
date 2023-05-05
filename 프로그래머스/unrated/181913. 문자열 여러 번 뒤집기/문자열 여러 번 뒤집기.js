function solution(my_string, queries) {
    var answer = my_string;
    
    for (let i = 0; i < queries.length; i++) {
        let start = queries[i][0]
        let end = queries[i][1]
        
        let temp = answer.substring(start, end + 1).split("").reverse().join("");
        
        // console.log('start', answer)
        // console.log(answer.substring(0, start))
        // console.log(answer.substring(start, end + 1))
        // console.log(answer.substring(end + 1, my_string.length))
                    
        answer = answer.substring(0, start) + temp + answer.substring(end + 1, my_string.length)
    }
    
    return answer;
}