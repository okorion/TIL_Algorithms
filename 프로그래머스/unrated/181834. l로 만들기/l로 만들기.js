function solution(myString) {
    const li = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"];
    
    return myString
        .split('')
        .map(char => li.includes(char) ? 'l' : char)
        .join('');
}
