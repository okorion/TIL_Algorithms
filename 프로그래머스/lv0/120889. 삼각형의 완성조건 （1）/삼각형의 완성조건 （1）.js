function solution(sides) {
    let tempList = [];
    
    tempList = sides.sort((a, b) => a - b)
    
    if (tempList[0] + tempList[1] > tempList[2]) return 1
    else return 2
}