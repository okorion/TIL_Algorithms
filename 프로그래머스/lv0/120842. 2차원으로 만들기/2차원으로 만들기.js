function solution(num_list, n) {
    var answer = [];
    
    for (let i = 0; i < num_list.length / n; i++) {
        let new_list = [...num_list]
        
        answer.push([...new_list.splice(i * n, n)])
    }
    
    return answer;
}