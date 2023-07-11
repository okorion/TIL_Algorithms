function solution(dots) {
    let answer = 0;
    
    dots = dots.sort()
    
    answer = (dots[1][1] - dots[0][1]) * (dots[2][0] - dots[0][0])
    console.log(dots)
    console.log(dots[1][1])
    return Math.abs(answer);
}