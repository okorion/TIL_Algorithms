function solution(emergency) {
  const sortedArray = [...emergency].sort((a, b) => b - a);
  const answer = emergency.map((item) => sortedArray.indexOf(item) + 1);
  return answer;
}