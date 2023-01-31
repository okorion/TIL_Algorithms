import sys
input = sys.stdin.readline

str_list = input()
asw = ""
stack = []

for _ in str_list:
    if _.isalpha():
        asw += _

    else:
        if _ == "-" or _ == "+":
            while stack and stack[-1] != "(":
                asw += stack.pop()
            stack.append(_)

        elif _ == "*" or _ == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                asw += stack.pop()
            stack.append(_)

        elif _ == "(":
            stack.append(_)

        elif _ == ")":
            while stack and stack[-1] != "(":
                asw += stack.pop()
            stack.pop()


while stack:
    asw += stack.pop()

print(asw)
