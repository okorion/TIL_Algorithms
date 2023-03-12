import sys

input = sys.stdin.readline

N = int(input())
data = list(map(lambda x: int(x) if x.isdigit() else x, input()))
result = -int(1e9)


def calc(num_a, num_b, operator):
    if operator == '+':
        return num_a + num_b
    elif operator == '-':
        return num_a - num_b
    elif operator == '*':
        return num_a * num_b


def dfs(idx, value):
    global result

    if idx >= N - 1:
        result = max(result, value)
        return

    if idx + 3 < N - 1:
        # print(idx, N)
        dfs(idx + 4, calc(value, calc(data[idx+2], data[idx+4], data[idx+3]), data[idx+1]))
    dfs(idx + 2, calc(value, data[idx+2], data[idx+1]))


if N == 1:
    result = data[0]
else:
    dfs(0, data[0])

print(result)
