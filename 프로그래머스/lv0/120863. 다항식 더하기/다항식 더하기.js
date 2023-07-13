function solution(polynomial) {
  const terms = polynomial.split(" + ");
  let coefficient = 0;
  let constant = 0;

  for (let term of terms) {
    if (term === "x") {
      coefficient += 1;
    } else if (term.endsWith("x")) {
      coefficient += parseInt(term.slice(0, -1));
    } else {
      constant += parseInt(term);
    }
  }

  if (coefficient === 0 && constant === 0) {
    return "0";
  } else if (coefficient !== 0 && constant === 0) {
    return coefficient === 1 ? "x" : `${coefficient}x`;
  } else if (coefficient === 0 && constant !== 0) {
    return `${constant}`;
  } else {
    const coefficientString = coefficient === 1 ? "x" : `${coefficient}x`;
    return `${coefficientString} + ${constant}`;
  }
}
