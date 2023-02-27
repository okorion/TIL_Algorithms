import sys
from collections import deque
input = sys.stdin.readline

N = int(input())


def bfs(n):
    queue = deque([[n]])

    while queue:
        temp = queue.popleft()
        a = temp[0]

        if a == 1:
            return temp

        if a % 3 == 0:
            queue.append([a // 3] + temp)

        if a % 2 == 0:
            queue.append([a // 2] + temp)

        queue.append([a - 1] + temp)


res = bfs(N)

print(len(res)-1)
print(*res[::-1])
