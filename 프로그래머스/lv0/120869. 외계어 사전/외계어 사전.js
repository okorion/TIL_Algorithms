function solution(spell, dic) {
    var answer = 0;
    
    for (let d of dic) {
        if (spell.every(i => d.split("").includes(i))) return 1
        
    }
    
    return 2;
}