import sys
input = sys.stdin.readline

temp_list = []

R, C = map(int, input().split())
visited = [[-1] * C for _ in range(R)]
count = 0
matrix = []

# print(visited)

for _ in range(R):
    matrix.append(list(input().strip()))

# print(matrix)


def dfs(x, y):
    if y == C - 1:
        return True

    for _ in [-1, 0, 1]:
        nx = _ + x
        ny = y + 1

        if 0 <= nx < R and 0 <= ny < C:
            if matrix[nx][ny] == '.' and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                # print(visited)
                if dfs(nx, ny):
                    return True
    return False


for _ in range(R):
    if dfs(_, 0):
        count += 1

print(count)
