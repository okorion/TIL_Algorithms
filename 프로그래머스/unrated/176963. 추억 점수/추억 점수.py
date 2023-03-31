def solution(name, yearning, photo):
    answer = []
    
    for _ in photo:
        temp_result = 0
        
        for idx, val in enumerate(name):
            for r in _:
                if r == val:
                    temp_result += yearning[idx]
                    
        answer.append(temp_result)
    
    return answer