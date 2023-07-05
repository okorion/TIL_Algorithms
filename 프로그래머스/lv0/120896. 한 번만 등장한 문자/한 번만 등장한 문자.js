function solution(s) {
  let object = {};
  var answer = '';
  
  // 알파벳들을 카운팅하여 object 객체에 저장
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    
    // 해당 알파벳이 object 객체에 없다면 초기값인 0으로 설정
    if (!object[char]) {
      object[char] = 0;
    }
    
    // 해당 알파벳 카운트 증가
    object[char] += 1;
  }
  
  console.log(object);
  
  // value가 1인 알파벳을 사전순으로 정렬하여 출력
  for (let key in object) {
    if (object[key] === 1) {
      answer += key;
    }
  }
  
  // 알파벳 정렬
  answer = answer.split('').sort().join('');
  
  return answer;
}

