def solution(my_string):
    answer = []
    
    for _ in my_string:
        try:
            answer.append(int(_))
        except ValueError:
            pass
    
    answer.sort()
    
    return answer