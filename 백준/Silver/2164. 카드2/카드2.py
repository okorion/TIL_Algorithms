import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

temp_list = deque()

for _ in range(1, N+1):
    temp_list.append(_)

# print(temp_list)

while len(temp_list) != 1:
    temp_list.popleft()
    temp_list.append(temp_list.popleft())

print(*temp_list)
