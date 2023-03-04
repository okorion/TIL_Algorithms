import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def eye_weak(temp_list):
    for _ in temp_list:
        for i in range(N):
            if _[i] == "G":
                _[i] = "R"


def dfs(tmp, x, y):
    global cnt

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    queue = deque([[x, y]])
    visited[x][y] = cnt
    # print(queue)
    while queue:
        p, q = queue.popleft()

        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]

            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == tmp and visited[nx][ny] == 0:
                    visited[nx][ny] = cnt
                    queue.append([nx, ny])


cnt = 1
answer = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(matrix[i][j], i, j)
            cnt += 1


answer.append(cnt - 1)
visited = [[0] * N for _ in range(N)]
eye_weak(matrix)
cnt = 1
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(matrix[i][j], i, j)
            cnt += 1

answer.append(cnt - 1)
# print(visited)
print(*answer)
