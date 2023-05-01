function solution(a, b, c, d) {
    const equals = (a, b) => JSON.stringify(a) === JSON.stringify(b);
    
    var answer = 0;
    let tmp = new Set([a, b, c, d])
    let tmp2 = Array.from(tmp)
    
    
    let countList = []
    
    for (let i = 0; i < tmp2.length; i++) {
        let count = [a, b, c, d].filter(element => tmp2[i] === element).length
        countList.push(count)
    }
    
    
    if (equals(countList, [4])) {
        answer = 1111 * a
    } else if (equals(countList, [3, 1])) {
        answer = (10 * tmp2[0] + tmp2[1]) ** 2
    } else if (equals(countList, [1, 3])) {
        answer = (10 * tmp2[1] + tmp2[0]) ** 2
    }else if (equals(countList, [2, 2])) {
        answer = (tmp2[0] + tmp2[1]) * Math.abs(tmp2[0] - tmp2[1])
    } else if (equals(countList, [2, 1, 1])) {
        answer = tmp2[1] * tmp2[2]
    } else if (equals(countList, [1, 2, 1])) {
        answer = tmp2[0] * tmp2[2]
    }else if (equals(countList, [1, 1, 2])) {
        answer = tmp2[0] * tmp2[1]
    }else {
        // console.log(tmp2)
        answer = Math.min(...tmp2)
    }
    
    return answer;
}