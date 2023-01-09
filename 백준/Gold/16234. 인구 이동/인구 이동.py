import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))


def bfs(a, b):
    queue = deque()
    temp_list = []

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    queue.append([a, b])
    temp_list.append([a, b])

    while queue:
        p, q = queue.popleft()

        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(matrix[nx][ny] - matrix[p][q]) <= R:
                    temp_list.append([nx, ny])
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

    return temp_list


result = 0
while 1:
    visited = [[0 for _ in range(N)] for k in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                if len(country) > 1:
                    flag = 1
                    num = sum([matrix[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        matrix[x][y] = num
    if flag == 0:
        break
    result += 1

print(result)