import sys

input = sys.stdin.readline

N = int(input())
input_list = list("".join(input().rstrip()))
temp_list = list(map(str, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
stack = []

for _ in range(N):
     temp_list.append(int(input()))


for i in input_list:
    if i == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif i == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif i == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif i == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    else:
        stack.append(temp_list[temp_list.index(i)+26])

print('%.2f' %stack[0])
