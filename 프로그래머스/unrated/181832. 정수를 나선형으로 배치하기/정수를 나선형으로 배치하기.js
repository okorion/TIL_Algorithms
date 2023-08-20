function solution(n) {
    const answer = new Array(n).fill().map(() => new Array(n).fill(0));

    let num = 1;
    let row = 0;
    let col = 0;
    let direction = 'right';

    while (num <= n * n) {
        answer[row][col] = num;
        num++;

        if (direction === 'right') {
            if (col + 1 < n && answer[row][col + 1] === 0) {
                col++;
            } else {
                direction = 'down';
                row++;
            }
        } else if (direction === 'down') {
            if (row + 1 < n && answer[row + 1][col] === 0) {
                row++;
            } else {
                direction = 'left';
                col--;
            }
        } else if (direction === 'left') {
            if (col - 1 >= 0 && answer[row][col - 1] === 0) {
                col--;
            } else {
                direction = 'up';
                row--;
            }
        } else if (direction === 'up') {
            if (row - 1 >= 0 && answer[row - 1][col] === 0) {
                row--;
            } else {
                direction = 'right';
                col++;
            }
        }
    }

    return answer;
}