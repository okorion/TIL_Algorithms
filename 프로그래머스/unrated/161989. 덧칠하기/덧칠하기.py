def solution(n, m, section):
    painting_list = [1] * (n + m)
    answer = 0
    
    for _ in section:
        painting_list[_ - 1] = 0
        
    for idx, val in enumerate(painting_list):
        if idx == n:
            break
        else:
            if val == 0:
                for paint in range(m):
                    painting_list[idx + paint] = 1
                answer += 1
    
    return answer