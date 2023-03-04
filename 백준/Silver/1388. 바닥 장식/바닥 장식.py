import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N + 1)]
visited = [[0] * M for _ in range(N + 1)]


def dfs(x, y):
    d = [1, -1]

    if matrix[x][y] == '-':
        visited[x][y] = 1
        for _ in range(2):
            ny = y + d[_]

            if 0 <= ny < M and matrix[x][ny] == '-' and visited[x][ny] == 0:
                dfs(x, ny)

    elif matrix[x][y] == '|':
        visited[x][y] = 2
        for _ in range(2):
            nx = x + d[_]

            if 0 <= nx < N and matrix[nx][y] == '|' and visited[nx][y] == 0:
                dfs(nx, y)


cnt = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1
# dfs(0, 0)
# print(visited)
print(cnt)
