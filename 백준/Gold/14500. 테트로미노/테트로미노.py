import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
max_value = -float('inf')
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[0] * M for _ in range(N)]


# def middle_tetromino(x, y):
#     global max_value
#
#     for _ in combinations(range(4), 3):
#         temp_sum = matrix[y][x]
#
#         for t in _:
#             nx = x + dx[t]
#             ny = y + dy[t]
#
#             if 0 <= nx < M and 0 <= ny < N:
#                 temp_sum += matrix[ny][nx]
#
#         max_value = max(max_value, temp_sum)


def tetromino(x, y, num, t_sum):   # ㅗ(욕 아님) 빼고 모든 경우
    global max_value

    if num == 3:
        max_value = max(max_value, t_sum)
        return

    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0:
                if num == 1:
                    visited[nx][ny] = 1
                    tetromino(x, y, num + 1, t_sum + matrix[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                tetromino(nx, ny, num + 1, t_sum + matrix[nx][ny])
                visited[nx][ny] = 0


for p in range(N):
    for q in range(M):
        visited[p][q] = 1
        tetromino(p, q, 0, matrix[p][q])
        visited[p][q] = 0
        # middle_tetromino(q, p)

print(max_value)
