function solution(array) {
    var l = array.length - 1
    let temp_array = array.sort((a,b) => a-b)
    
    console.log(temp_array)
    return temp_array[l/2];
}