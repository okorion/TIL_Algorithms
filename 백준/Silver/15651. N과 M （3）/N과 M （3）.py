import sys

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N + 1)
result_list = []


def n_and_m(k, n, m):
    if k == m:
        # return print(*result_list)
        return print(" ".join(map(str, result_list)))

    for num in range(1, n+1):
        if not visited[num]:
            result_list.append(num)
            # visited[num] = True
            n_and_m(k+1, n, m)
            result_list.pop()
            # visited[num] = False


n_and_m(0, N, M)
