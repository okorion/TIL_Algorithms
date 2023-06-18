function solution(money) {
    var answer = [];
    
    americano = parseInt(money / 5500)
    
    answer.push(americano)
    answer.push(money - americano * 5500)
    
    return answer;
}