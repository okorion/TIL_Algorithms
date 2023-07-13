function solution(keyinput, board) {
    let answer = [0, 0]; // 캐릭터의 시작 좌표
    const centerX = Math.floor((board[0] - 1) / 2); // 보드의 가로 중앙 좌표
    const centerY = Math.floor((board[1] - 1) / 2); // 보드의 세로 중앙 좌표
    
    for (let key of keyinput) {
        if (key === "left" && answer[0] > -centerX) {
            answer[0] -= 1; // 왼쪽으로 이동
        }
        if (key === "right" && answer[0] < centerX) {
            answer[0] += 1; // 오른쪽으로 이동
        }
        if (key === "down" && answer[1] > -centerY) {
            answer[1] -= 1; // 아래로 이동
        }
        if (key === "up" && answer[1] < centerY) {
            answer[1] += 1; // 위로 이동
        }
    }
    
    return answer;
}
