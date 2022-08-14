import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp_list = [0] + sorted(list(map(int, input().split())))
result_list = []


def backtracking(k, n, m):
    if len(result_list) == m:
        return print(" ".join(map(str, result_list)))

    for num in range(1, n+1):
        if len(result_list) > 0:
            if temp_list[num] < result_list[-1]:
                continue
        result_list.append(temp_list[num])
        backtracking(k+1, n, m)
        result_list.pop()


backtracking(0, N, M)
