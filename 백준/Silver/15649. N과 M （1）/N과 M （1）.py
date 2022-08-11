import sys

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N+1)
result_list = []


def backtracking(k, n, m):
    if k == m:
        return print(" ".join(map(str, result_list)))   # print(*result_list)

    for i in range(1, n+1):
        if not visited[i]:
            result_list.append(i)
            visited[i] = True
            backtracking(k+1, n, m)
            result_list.pop()
            visited[i] = False


backtracking(0, N, M)
