import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

N, M = map(int, input().split())

temp_matrix = []

for _ in range(N):
    temp_matrix.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def outside():
    dq = deque()
    visited = [[0] * M for _ in range(N)]
    dq.append((0, 0))
    visited[0][0] = 1
    temp_matrix[0][0] = -1
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if temp_matrix[nx][ny] != 1 and visited[nx][ny] == 0:
                    dq.append((nx, ny))
                    temp_matrix[nx][ny] = -1
                    visited[nx][ny] = 1
    return


def dfs(matrix):
    global result

    queue = deque()
    for a in range(N):
        for b in range(M):
            if matrix[a][b] == 1:
                queue.append([a, b])
    # visited = [[0 for a in range(M)] for b in range(N)]

    while queue:
        p, q = queue.popleft()

        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == -1:
                    matrix[p][q] += 1
    result += 1


result = 0

while True:
    outside()
    dfs(temp_matrix)
    for a in range(N):
        for b in range(M):
            if temp_matrix[a][b] >= 3:
                temp_matrix[a][b] = 0
            elif temp_matrix[a][b] == 2:
                temp_matrix[a][b] = 1
            elif temp_matrix[a][b] == -1:
                temp_matrix[a][b] = 0
    if sum([sum(_) for _ in temp_matrix]) == 0:
        break

print(result)
