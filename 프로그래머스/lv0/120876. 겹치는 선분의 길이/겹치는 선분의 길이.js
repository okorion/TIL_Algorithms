function solution(lines) {
    let answer = 0;
    let tmpList = [];
    
    for (let i = 0; i < 200; i++) {
        tmpList[i] = 0;
    }
    
    for (let line of lines) {
        let start = line[0] + 100
        let end = line[1] + 100
        
        for (let k = start; k < end; k++) {
            tmpList[k] += 1
        }
    }
    
    return tmpList.filter(n => n >= 2).length;
}