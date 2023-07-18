function solution(n) {
    let cnt = 0;
    let num = 0;
    
    while (true) {
        if (cnt === n) return num
        else if (cnt !== n) {
            while (true) {
                num++
                if (num % 3 && !String(num).includes('3')) {
                    break
                }
            }
            cnt++
        }
    }
}