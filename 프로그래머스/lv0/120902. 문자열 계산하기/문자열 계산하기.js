function solution(my_string) {
  let answer = 0;
  let numbers = my_string.split(" ");

  let isAddition = true;

  for (let i = 0; i < numbers.length; i++) {
    const current = Number(numbers[i]);

    if (isNaN(current)) {
      isAddition = numbers[i] === "+";
    } else {
      answer += isAddition ? current : -current;
    }
  }

  return answer;
}
