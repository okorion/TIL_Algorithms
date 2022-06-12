import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

temp_list = deque()
result_list = []

for _ in range(1, N+1):
    temp_list.append(_)

for _ in range(N):
    temp_list.rotate(-K+1)
    result_list.append(str(temp_list.popleft()))

print(f"<{', '.join(result_list)}>")
