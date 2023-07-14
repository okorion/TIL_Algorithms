function solution(my_string) {
  my_string = my_string + "O";
  let answer = 0;
  let tmp = "";

  for (let i = 0; i < my_string.length; i++) {
    const currentChar = my_string[i];
    if (!isNaN(Number(currentChar))) {
      tmp += currentChar;
    } else {
      if (tmp.length !== 0) {
        answer += Number(tmp);
        tmp = "";
      }
    }
  }

  return answer;
}
