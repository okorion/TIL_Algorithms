def solution(a, b):
    answer = 0
    
    if a <= b:
        for _ in range(a, b+1):
            answer += _
    else:
        for _ in range(b, a+1):
            answer += _
    
    return answer