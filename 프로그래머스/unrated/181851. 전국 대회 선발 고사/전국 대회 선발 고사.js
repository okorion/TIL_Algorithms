function solution(rank, attendance) {
    var answer = 0;
    let temp = [];
    let n = 3
    
    for (let i = 1; i < attendance.length + 1; i++) {
        const ranker = rank.indexOf(i)
        
        if (attendance[ranker]) {
            answer += ranker * (10 ** (2 * n - 2))
            n--
        }
        
        if (n === 0) return answer;
    }
}