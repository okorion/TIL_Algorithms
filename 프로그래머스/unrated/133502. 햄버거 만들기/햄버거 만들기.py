def solution(ingredient):
    answer = 0
    stack = []
    
    for _ in ingredient:
        stack.append(_)
        
        if len(stack) >= 4:
            if stack[-1] == 1:
                # print(stack, stack[len(stack)-4:len(stack)])
                if stack[len(stack)-4:len(stack)] == [1, 2, 3, 1]:
                    answer += 1

                    for t in range(4):
                        stack.pop()

    return answer