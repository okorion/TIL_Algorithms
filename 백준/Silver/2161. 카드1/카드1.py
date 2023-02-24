import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
temp_list = deque(range(1, N+1))
result = []

# print(temp_list)

while True:
    if len(temp_list) > 1:
        result.append(temp_list.popleft())
        temp_list.append(temp_list.popleft())
        # print(temp_list)
    else:
        result.append(temp_list[0])
        break

print(*result)
