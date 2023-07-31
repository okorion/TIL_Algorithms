function solution(arr, intervals) {
    var answer = [];
    
    for (let i = 0; i < intervals.length; i++) {
        let [start, end] = intervals[i];
        let intervalArr = arr.slice(start, end + 1);
        answer = answer.concat(intervalArr);
    }
    
    return answer;
}
