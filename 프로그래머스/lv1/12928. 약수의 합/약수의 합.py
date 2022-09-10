def solution(n):
    sum = 0
    for _ in range(1, n+1):
        if n % _ == 0:
            sum += _
    
    return sum
