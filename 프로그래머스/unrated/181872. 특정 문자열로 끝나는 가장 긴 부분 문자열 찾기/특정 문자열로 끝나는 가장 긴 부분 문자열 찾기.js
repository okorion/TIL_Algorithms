function solution(myString, pat) {
  let longestEndingWithPat = '';

  for (let i = 0; i < myString.length + 1; i++) {
    if (myString.slice(0, i).endsWith(pat)) {
      longestEndingWithPat = myString.slice(0, i);
    }
  }

  return longestEndingWithPat;
}