import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1

queue = deque()
answer = []

for _ in range(1, N + 1):
    if degree[_] == 0:
        queue.append(_)

while queue:
    temp = queue.popleft()
    answer.append(temp)

    for _ in graph[temp]:
        degree[_] -= 1

        if degree[_] == 0:
            queue.append(_)

print(*answer)
