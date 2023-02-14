import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())  #건물개수 N, 규칙 총 개수 K
    time_list = [0] + list(map(int, input().split()))   #건설에 걸리는 시간 D1~DN
    degree = [0] * (N + 1)
    structure_pr = [[] for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]

    for k in range(K):
        a, b = map(int, input().split())
        structure_pr[a].append(b)
        degree[b] += 1

    W = int(input())  # 승리 건물 번호

    queue = deque()

    for _ in range(1, N + 1):
        if degree[_] == 0:
            queue.append(_)
            dp[_] = time_list[_]

    while queue:
        temp = queue.popleft()

        for _ in structure_pr[temp]:
            degree[_] -= 1
            dp[_] = max(dp[temp] + time_list[_], dp[_])

            if degree[_] == 0:
                queue.append(_)

    print(dp[W])
