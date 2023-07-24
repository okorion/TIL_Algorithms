function solution(bin1, bin2) {
  let result = '';
  let carry = 0;
  let i = bin1.length - 1;
  let j = bin2.length - 1;

  while (i >= 0 || j >= 0 || carry > 0) {
    const digit1 = i >= 0 ? parseInt(bin1[i]) : 0;
    const digit2 = j >= 0 ? parseInt(bin2[j]) : 0;

    const sum = digit1 + digit2 + carry;
    const currentDigit = sum % 2;
    carry = Math.floor(sum / 2);

    result = currentDigit + result;

    i--;
    j--;
  }

  return result;
}