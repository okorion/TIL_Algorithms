function solution(num_list) {
    var answer = [0, 0];
    
    for (let i = 0; i < num_list.length; i++) {
        if (num_list[i] % 2) {
            answer[1] += 1
        } else {
            answer[0] += 1
        }
    }
    
    return answer;
}