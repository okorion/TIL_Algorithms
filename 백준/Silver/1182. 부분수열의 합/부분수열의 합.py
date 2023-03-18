import sys

input = sys.stdin.readline

N, S = map(int, input().split())
temp_list = list(map(int, input().split()))
answer = 0


def dfs(idx, val):
    global answer

    if idx >= N:
        return

    val += temp_list[idx]

    if val == S:
        answer += 1

    dfs(idx + 1, val)
    dfs(idx + 1, val - temp_list[idx])


dfs(0, 0)

print(answer)
