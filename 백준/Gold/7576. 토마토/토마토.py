import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited_matrix = [[0 for _ in range(M)] for k in range(N)]

# print(matrix)
# print(visited_matrix)

queue = deque()


def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        p, q = queue.popleft()

        for _ in range(4):  # M = i = q = ny, N = j = p = nx
            nx = p + dx[_]
            ny = q + dy[_]
            if 0 <= ny < M and 0 <= nx < N:
                if matrix[nx][ny] == 0 and visited_matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[p][q] + 1
                    visited_matrix[p][q] = 1
                    queue.append([nx, ny])


for i in range(M):
    for j in range(N):
        if matrix[j][i] == 1:
            queue.append([j, i])

bfs()
# print(matrix)
# print(visited_matrix) #visited 필요 X
result = 0

for a in matrix:
    for b in a:
        if b == 0:
            print(-1)
            exit(0)
    result = max(result, max(a))

print(result - 1)