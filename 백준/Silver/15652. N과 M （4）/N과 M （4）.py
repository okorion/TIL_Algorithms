import sys


input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N + 1)
result_list = []


def n_and_m(k, n, m):
    if k == m:
        return print(" ".join(map(str, result_list)))

    for num in range(1, n+1):
        if len(result_list) > 0:
            if num < result_list[-1]:
                continue
        result_list.append(num)
        n_and_m(k+1, n, m)
        result_list.pop()


n_and_m(0, N, M)
