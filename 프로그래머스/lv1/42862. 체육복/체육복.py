def solution(n, lost, reserve):
    answer = 0
    temp_list = [1] * n
    
    lost.sort()
    reserve.sort()
    
    for _ in lost:
        temp_list[_ - 1] -= 1
        
    for _ in reserve:
        temp_list[_ - 1] += 1
        
    for idx, val in enumerate(temp_list):
        if val == 0:                
            if idx - 1 >= 0 and temp_list[idx - 1] == 2:
                temp_list[idx - 1] -= 1
                temp_list[idx] += 1
                
            elif idx + 1 < n and temp_list[idx + 1] == 2:
                temp_list[idx + 1] -= 1
                temp_list[idx] += 1
    
    print(temp_list)
    answer = n - temp_list.count(0)
    
    return answer