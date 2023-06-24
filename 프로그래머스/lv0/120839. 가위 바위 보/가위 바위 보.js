function solution(rsp) {
    let answer = '';
    let gababo = {
        "2": "0",
        "0": "5",
        "5": "2"
    }
    
    for (let i = 0; i < rsp.length; i++) {
        answer += gababo[rsp[i]]
    }
    
    return answer;
}