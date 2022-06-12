import sys
from collections import deque

N = int(sys.stdin.readline())

deque = deque()

for _ in range(N):
    a = str(sys.stdin.readline().strip())

    if 'push' in a:
        b = list(a.split())
        deque.append(int(b[1]))

    elif 'size' in a:
        print(len(deque))

    elif 'pop' in a:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())

    elif 'empty' in a:
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif 'front' in a:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif 'back' in a:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
