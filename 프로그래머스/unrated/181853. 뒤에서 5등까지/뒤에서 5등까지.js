function solution(num_list) {
    return num_list.map(i => parseInt(i)).sort((a, b) => a - b).slice(0, 5);
}
