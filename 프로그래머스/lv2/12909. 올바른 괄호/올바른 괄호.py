def solution(s):
    stack = []
    flag = True
    
    for _ in s:
        if _ == "(":
            stack.append(_)
        elif _ == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
    
    if stack:
        flag = False
    
    return flag