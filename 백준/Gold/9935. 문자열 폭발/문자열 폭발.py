import sys

input = sys.stdin.readline

temp_str = str(input().strip())
temp_word = str(input().strip())
N = len(temp_str)
M = len(temp_word)
stack = []

# print(N, M)

for _ in temp_str:
    stack.append(_)
    if ''.join(stack[-M:]) == temp_word:
        for n in range(M):
            # print(stack)
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
