def solution(M, N):
    tmp_a, tmp_b = min(M, N), max(M, N)
    
    answer = (tmp_a) * (tmp_b - 1) + (tmp_a - 1)
    
    
    return answer