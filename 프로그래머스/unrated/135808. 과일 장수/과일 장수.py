def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for _ in range(len(score) // m):
        answer += score[_ * m + (m - 1)] * m
    
    return answer