function solution(board) {
    let newArray = []
    var answer = 0;
    let tmp = [-1, 0, 1]
    
    newArray = [...board]
    
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board.length; j++) {
            if (board[i][j] === 1) {
                for (let a of tmp) {
                    for (let b of tmp) {
                        if (i+a >= 0  && i+a < board.length && j+b >= 0  && j+b < board.length) { 
                            if (board[i+a][j+b] === 0) newArray[i+a][j+b] = 2
                        }
                    }                    
                }
            }
        }
    }
    
    answer = newArray.flat(Infinity).filter(i => i === 0).length
    
    return answer;
}