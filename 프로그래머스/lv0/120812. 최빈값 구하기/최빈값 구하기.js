function solution(array) {
  var answer = 0;
  var tmp_json = {};

  for (let i = 0; i < array.length; i++) {
    if (!tmp_json[array[i]]) {
      tmp_json[array[i]] = 1;
    } else {
      tmp_json[array[i]] += 1;
    }
  }

  console.log(tmp_json);
  var max_value = 0;
  var isDuplicate = true;
    

  for (let key of Object.keys(tmp_json)) {
    var tmp = tmp_json[key];
    if (tmp > max_value) {
      max_value = tmp;
        answer = key
      isDuplicate = false;
    } else if (tmp === max_value) {
      isDuplicate = true;
    }
  }
  return isDuplicate ? -1 : Number(answer);
}