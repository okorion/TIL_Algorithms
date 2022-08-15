import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp_list = [0] + sorted(list(map(int, input().split())))
result_list = []


def backtracking(k, n, m):
    if k == m:
        return print(*result_list)

    remember_num = 0
    for num in range(1, N+1):
        if remember_num != temp_list[num]:
            if len(result_list) > 0:
                if temp_list[num] < result_list[-1]:
                    continue
            remember_num = temp_list[num]
            result_list.append(temp_list[num])
            backtracking(k+1, n, m)
            result_list.pop()


backtracking(0, N, M)