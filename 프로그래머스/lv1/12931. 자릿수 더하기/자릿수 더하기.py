def solution(N):
    string = str(N)
    sum = 0
    temp = map(int, string)
    
    for _ in temp:
        sum += _
    
    return sum