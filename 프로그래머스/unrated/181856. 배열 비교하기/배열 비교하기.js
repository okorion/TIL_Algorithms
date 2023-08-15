function solution(arr1, arr2) {
    var answer = 0;
    let lengthArr1 = arr1.length
    let lengthArr2 = arr2.length
    let totalArr1 = arr1.reduce((a, b) => a + b)
    let totalArr2 = arr2.reduce((a, b) => a + b)
    
    if (lengthArr1 > lengthArr2) return 1
    if (lengthArr1 < lengthArr2) return -1
    if (lengthArr1 === lengthArr2) {
        if (totalArr1 > totalArr2) return 1
        if (totalArr1 < totalArr2) return -1
        if (totalArr1 === totalArr2) return 0
    }
    
}