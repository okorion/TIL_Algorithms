function solution(before, after) {
    let tempA = {};
    let tempB = {};
    
      for (let t of before.split("")) {
        tempA[t] = (tempA[t] || 0) + 1;
      }

      for (let t of after.split("")) {
        tempB[t] = (tempB[t] || 0) + 1;
      }
    
    // 두 객체의 키와 값을 비교하여 동등성을 확인합니다.
    const keysA = Object.keys(tempA);
    const keysB = Object.keys(tempB);

    return keysA.some(i => tempA[i] !== tempB[i]) ? 0 : 1

}