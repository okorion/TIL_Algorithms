import sys

input = sys.stdin.readline

N, M = map(int, input().split())
test_list = [0] + sorted(list(map(int, input().split())))
visited = [False] * (N + 1)
result_list = []


def backtracking(k, n, m):
    if k == m:
        return print(*result_list)

    for num in range(1, N+1):
        if not visited[num]:
            visited[num] = True
            result_list.append(test_list[num])
            backtracking(k+1, n, m)
            visited[num] = False
            result_list.pop()


backtracking(0, N, M)
