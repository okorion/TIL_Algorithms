def solution(s):
    answer = []
    temp_list = []
    
    for idx, val in enumerate(s):
        temp_list.append(val)
        
        if temp_list.count(val) == 1:
            answer.append(-1)
        else:
            # print(temp_list, temp_list[-2::-1], idx)
            answer.append(temp_list[-2::-1].index(val) + 1)
    
    return answer