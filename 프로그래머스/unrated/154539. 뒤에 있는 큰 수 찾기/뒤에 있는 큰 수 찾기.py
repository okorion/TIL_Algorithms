def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for a, b in enumerate(numbers):
        while stack and numbers[stack[-1]] < numbers[a]:
            answer[stack.pop()] = numbers[a]
        stack.append(a)

    return answer