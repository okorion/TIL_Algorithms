import sys

input = sys.stdin.readline

while True:
    stack = []
    temp = input().rstrip()
    result = True

    if temp == '.':
        break

    for _ in temp:
        if _ == '(' or _ == '[':
            stack.append(_)
        elif _ == ')':
            if not stack or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif _ == ']':
            if not stack or stack[-1] == '(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if result == True and not stack:
        print('yes')
    else:
        print('no')
