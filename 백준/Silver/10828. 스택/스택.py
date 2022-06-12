import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    a = str(sys.stdin.readline().strip())

    if 'push' in a:
        b = list(a.split())
        stack.append(int(b[1]))

    elif 'top' in a:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif 'size' in a:
        print(len(stack))

    elif 'pop' in a:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))

    elif 'empty' in a:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
