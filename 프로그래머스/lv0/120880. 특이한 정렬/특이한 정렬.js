function solution(numlist, n) {
  const distanceComparator = (a, b) => {
    const distanceA = Math.abs(a - n);
    const distanceB = Math.abs(b - n);

    if (distanceA !== distanceB) {
      return distanceA - distanceB;
    } else {
      // 거리가 같을 경우 양수를 우선하고, 양수가 아니라면 더 큰 수를 우선하여 정렬합니다.
      return a < 0 ? 1 : b < 0 ? -1 : b - a;
    }
  };

  const sortedNums = numlist.slice().sort(distanceComparator);
  const output = [];

  for (const num of sortedNums) {
    output.push(num);
  }

  return output;
}