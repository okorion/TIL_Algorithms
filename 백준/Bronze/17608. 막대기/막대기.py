import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    stack.append(int(sys.stdin.readline()))

# print(stack)
Max = 0
cnt = 0

for _ in range(N-1, -1, -1):
    if stack[_] > Max:
        Max = stack[_]
        cnt += 1

print(cnt)
