def solution(sizes):
    answer = 0
    min_list = []
    max_list = []
    
    for _ in sizes:
        min_list.append(min(_))
        max_list.append(max(_))
    
    answer = max(min_list) * max(max_list)
    
    return answer