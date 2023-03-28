def solution(numbers):
    answer = []
    l = len(numbers)
    
    for start in range(l - 1):
        for end in range(start + 1, l):
            answer.append(numbers[start] + numbers[end])
    
    answer = list(set(answer))
    answer.sort()
    
    return answer