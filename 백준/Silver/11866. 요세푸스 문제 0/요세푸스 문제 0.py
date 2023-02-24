import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
answer = []

for _ in range(1, N+1):
    queue.append(_)

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print(f'<{str(answer).lstrip("[").rstrip("]")}>')
