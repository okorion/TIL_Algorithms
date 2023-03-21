import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
temp_list = list(map(int, input().split()))
queue = deque()
count = 0

for _ in range(1, N + 1):
    queue.append(_)

# print(queue)

for _ in temp_list:
    while True:
        if queue[0] == _:
            queue.popleft()
            break

        else:
            if queue.index(_) <= len(queue) // 2:
                queue.rotate(-1)
                count += 1
            else:
                queue.rotate(1)
                count += 1

print(count)
