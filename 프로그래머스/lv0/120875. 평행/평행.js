function slope(p1, p2) {
  // 기울기를 구하기 전에 분모가 0인 경우를 처리해야 합니다.
  if (p1[0] === p2[0]) return Infinity; // x 좌표가 같으면 수직 선분, 기울기 무한대
  return (p2[1] - p1[1]) / (p2[0] - p1[0]);
}
  // ChatGPT
function solution(dots) {
  for (let i = 0; i < 3; i++) {
    for (let j = i + 1; j < 4; j++) {
      const slope1 = slope(dots[i], dots[j]);
      for (let k = i + 1; k < 4; k++) {
        if (k === j) continue;
        for (let l = k + 1; l < 4; l++) {
          if (l === i || l === j) continue;
          const slope2 = slope(dots[k], dots[l]);
          if (slope1 === slope2) return 1;
        }
      }
    }
  }

  return 0;
}