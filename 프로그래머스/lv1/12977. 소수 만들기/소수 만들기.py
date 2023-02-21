from itertools import combinations

def is_num(num):
    for _ in range(2, num//2 + 1):
        if num % _ == 0:
            return True
        
    return False


def solution(nums):
    cnt = 0
    
    temp_numlist = combinations(nums, 3)
    
    for _ in temp_numlist:
        if not is_num(sum(_)):
            cnt += 1
            # print(sum(_))
    
    return cnt
