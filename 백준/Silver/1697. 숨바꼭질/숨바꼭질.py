import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
result_list = deque()
result_list.append(N)
dist = [0] * 100001

while True:
    t = result_list.popleft()

    if t == K:
        print(dist[t])
        break

    for _ in (t - 1, t + 1, t * 2):
        if 0 <= _ <= 100000 and not dist[_]:
            dist[_] = dist[t] + 1
            result_list.append(_)

