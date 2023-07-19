function gcd(a, b) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}

function solution(a, b) {
    let num = gcd(a, b)
    let ans = b / num
    
    while (ans % 2 === 0) {
        ans = ans / 2;
        }
    
    while (ans % 5 === 0) {
        ans = ans / 5;
        }
    
    return ans === 1 ? 1 : 2;
}