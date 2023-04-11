def solution(n):
    temp_list = [0] + [1] * (n)
    
    for _ in range(2, n + 1):
        if temp_list[_ - 1] == 1:
            for t in range(2 * _, n + 1, _):
                temp_list[t - 1] = 0
                    
    answer = temp_list.count(1) - 1
    
    return answer