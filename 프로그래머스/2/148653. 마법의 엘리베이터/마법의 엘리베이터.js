function solution(storey) {
    let magicStones = 0
    
    while (storey > 0) {
        let currentDigit = storey % 10
        let nextDigit = Math.floor(storey / 10) % 10
        
        if (currentDigit > 5 || currentDigit === 5 && nextDigit >= 5) {
            magicStones += (10 - currentDigit)
            storey = Math.floor(storey / 10) + 1
        } else {
            magicStones += currentDigit
            storey = Math.floor(storey / 10)
        }
    }
    
    return magicStones;
}
