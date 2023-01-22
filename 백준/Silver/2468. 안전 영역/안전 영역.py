import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

matrix = []
visited = [[0] * N for _ in range(N)]
max_val = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))
    for k in range(N):
        if matrix[_][k] > max_val:
            max_val = matrix[_][k]


def bfs(i, j, height):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        p, q = queue.popleft()

        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]

            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] > height and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])


result = 0

for rain in range(max_val):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for a in range(N):
        for b in range(N):
            if matrix[a][b] > rain and visited[a][b] == 0:
                bfs(a, b, rain)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)
