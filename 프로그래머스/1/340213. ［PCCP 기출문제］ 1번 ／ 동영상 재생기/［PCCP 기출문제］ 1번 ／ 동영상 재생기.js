function converter(time_string) {
    return Number(time_string.split(":")[0]) * 60 + Number(time_string.split(":")[1]);
}

function isOpenning(time, op_start, op_end) {
    return time >= op_start && time <= op_end;
}

function stdTimeString(num) {
    return num < 10 ? "0" + num : String(num);
}

function solution(video_len, pos, op_start, op_end, commands) {
    const video_len_num = converter(video_len);
    let result_num = converter(pos);
    const op_start_num = converter(op_start);
    const op_end_num = converter(op_end);
    
    if (isOpenning(result_num, op_start_num, op_end_num)) {
        result_num = op_end_num
    }
    
    commands.forEach((command) => {
        if (command === "next") {
            result_num += 10;
            if (result_num > video_len_num) {
                result_num = video_len_num;
            }
        } else if (command === "prev") {
            result_num -= 10;
            if (result_num < 0) {
                result_num = 0;
            }
        }
        
        // 오프닝 구간에 위치할 경우 자동으로 오프닝 끝으로 이동
        if (isOpenning(result_num, op_start_num, op_end_num)) {
            result_num = op_end_num;
        }
    });

    const minutes = stdTimeString(Math.floor(result_num / 60));
    const seconds = stdTimeString(result_num % 60);
    return `${minutes}:${seconds}`;
}
