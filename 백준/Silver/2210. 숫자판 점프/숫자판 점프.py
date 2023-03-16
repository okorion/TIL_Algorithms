import sys

input = sys.stdin.readline

matrix = [list(map(str, input().split())) for _ in range(5)]

# print(matrix)

result = []


def dfs(x, y, num):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

    if len(num) == 6:   # if len(num) == 6 and num not in result: 로 작성하면 뒤의 조건을 만족 못할 시 계속 재귀.
        if num not in result:
            result.append(num)
        return

    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + matrix[nx][ny])


for a in range(5):
    for b in range(5):
        dfs(a, b, matrix[a][b])

print(len(result))
