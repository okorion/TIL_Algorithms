import sys

input = sys.stdin.readline

N = int(input())
cal_list = list(input().split() for _ in range(N))

max_result = -(5 ** 20)
min_result = 5 ** 20

result_list = []


def dfs(y, x, curr_num, before):
    global max_result, min_result

    dx = [1, 0]
    dy = [0, 1]

    if x == N - 1 and y == N - 1:
        max_result = max(max_result, int(curr_num))
        min_result = min(min_result, int(curr_num))

    for _ in range(2):
        nx = x + dx[_]
        ny = y + dy[_]

        if 0 <= nx < N and 0 <= ny < N:
            if cal_list[ny][nx].isdigit():
                dfs(ny, nx, str(eval(curr_num + before + cal_list[ny][nx])), "")
            else:
                dfs(ny, nx, curr_num, cal_list[ny][nx])


dfs(0, 0, cal_list[0][0], "")
print(max_result, min_result)
