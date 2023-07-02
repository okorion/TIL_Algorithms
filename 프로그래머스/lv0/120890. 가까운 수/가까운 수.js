function solution(array, n) {
    var answer = 1000000;
    let tmp = 0;
    
    for (let i = 0; i < array.length; i++) {
        if (Math.abs(array[i] - n) < answer) {
            tmp = array[i]
            answer = Math.abs(array[i] - n)
        } else if (Math.abs(array[i] - n) === answer) {
            if (tmp > array[i]) tmp = array[i]
        }
    }
    
    return tmp;
}