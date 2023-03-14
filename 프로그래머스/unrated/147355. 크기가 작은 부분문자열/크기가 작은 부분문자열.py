def solution(t, p):
    answer = 0
    
    for _ in range(len(t)-len(p)+1):
        temp = ""
        for k in range(len(p)):
            temp += t[_ + k]
        if int(temp) <= int(p):
            answer += 1
        print(temp, p)
    
    return answer