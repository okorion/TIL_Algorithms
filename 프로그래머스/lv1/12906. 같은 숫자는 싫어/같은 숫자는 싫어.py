def solution(arr):
    length = len(arr)
    temp_num = -1
    result_list = []
    
    for i in range(length):
        if arr[i] != temp_num:
            temp_num = arr[i]
            result_list.append(arr[i])
        else:
            pass
    return result_list