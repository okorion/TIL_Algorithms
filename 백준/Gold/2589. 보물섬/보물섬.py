import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []


def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    max_value = 0

    while queue:
        p, q = queue.popleft()
        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 'L':
                    visited[nx][ny] = visited[p][q] + 1
                    queue.append([nx, ny])
                    max_value = max(max_value, visited[nx][ny])

    return max_value


for _ in range(N):
    matrix.append(list(input().strip()))

# print(matrix)
# print(visited)

temp_list = []
result = 0

for a in range(N):
    for b in range(M):
        if matrix[a][b] == 'L':
            result = max(result, bfs(a, b))

print(result - 1)
