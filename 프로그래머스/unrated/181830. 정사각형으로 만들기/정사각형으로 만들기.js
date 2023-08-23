function solution(arr) {
    var answer = [...arr];
    var row = arr[0].length;
    var col = arr.length;
    
    if (row === col) return arr
    else if (row > col) {
        for (let i = 0; i < row - col; i++) {
            answer.push(Array(row).fill(0))
        }
        
        return answer
    }
    else if (row < col) {
        for (let a of answer) {
            for (let j = 0; j < col - row; j++) {
                a.push(0)
            }
        }
        return answer
    }
}