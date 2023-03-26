def solution(food):
    answer = ''
    
    for idx, val in enumerate(food):
        answer += str(idx) * (val // 2)
        print(str(idx) * (val//2))
    
    answer += '0'
    answer2 = answer
    
    for _ in range(len(answer) - 2, -1, -1):
        answer2 += answer[_]
        
    return answer2