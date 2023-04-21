def solution(order):
    answer = 0
    
    for o in order:
        if "cafelatte" in o:
            answer += 5000
        elif "americano" in o:
            answer += 4500
        elif "anything" in o:
            answer += 4500
    
    return answer