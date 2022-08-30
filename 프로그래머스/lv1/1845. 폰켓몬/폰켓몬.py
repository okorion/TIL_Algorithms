def solution(nums):
    temp_len = len(nums)
    temp_result = temp_len // 2
    temp_set = set(nums)
    
    if len(temp_set) < temp_result:
        return len(temp_set)
    else:
        return temp_result