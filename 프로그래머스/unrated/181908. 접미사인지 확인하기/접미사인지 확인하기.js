function solution(my_string, is_suffix) {
    let answer = 0;
    let ans = ""
    
    for (let i = my_string.split("").length - is_suffix.split("").length; i < my_string.split("").length; i++) {
        ans += my_string[i]
    }
    
    if (ans === is_suffix) {
        return 1;
    } else {
        return 0;
    }
}