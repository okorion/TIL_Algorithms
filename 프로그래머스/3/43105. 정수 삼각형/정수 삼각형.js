function solution(triangle) {
    var answer = 0;
    
    for (let i = 0; i < triangle.length; i++) {
        if (i > 0) {
            for (let j = 0; j < i + 1; j++) { 
                if (j === 0) {
                    triangle[i][j] += triangle[i-1][j]
                } else if (j === i) {
                    triangle[i][j] += triangle[i-1][j-1]
                } else {
                    triangle[i][j] += Math.max(triangle[i-1][j-1], triangle[i-1][j])
                }
            }
        }
    }
    
    answer = Math.max(...triangle[triangle.length - 1])
    
    return answer;
}