def solution(a, b):
    result = 0
    for _ in range(len(a)):
        result += a[_] * b[_]
        
    return result
