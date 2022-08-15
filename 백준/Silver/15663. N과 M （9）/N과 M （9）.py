import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp_list = [0] + sorted(list(map(int, input().split())))
result_list = []
visited = [0] * (N + 1)


def backtracking(k, n, m):
    if k == m:
        return print(*result_list)

        # return print(" ".join(map(str, result_list)))
    remember_num = 0

    for num in range(1, N+1):
        if not visited[num] and temp_list[num] != remember_num:
            result_list.append(temp_list[num])
            visited[num] += 1
            remember_num = temp_list[num]
            backtracking(k+1, n, m)
            result_list.pop()
            visited[num] -= 1


backtracking(0, N, M)
