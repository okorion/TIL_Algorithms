import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

matrix = [[] for i in range(H)]
for i in range(H):
    for j in range(N):
        matrix[i].append(list(map(int, input().split())))


visited = [[[0 for i in range(M)] for j in range(N)] for k in range(H)]
queue = deque()

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def spread_tomato():
    # 1이 있는 토마토가 6면으로 0을 1로 만드는 작업. -1은 무시
    while queue:
        i, j, h = queue.popleft()
        visited[h][i][j] = 1

        for _ in range(6):
            nx = i + dx[_]
            ny = j + dy[_]
            nz = h + dz[_]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and matrix[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                matrix[nz][nx][ny] = matrix[h][i][j] + 1
                visited[nz][nx][ny] = 1
                queue.append([nx, ny, nz])


for a in range(H):
    for b in range(N):
        for c in range(M):
            if matrix[a][b][c] == 1:
                queue.append([b, c, a])

spread_tomato()
result = 0
temp = False

for a in range(H):
    for b in range(N):
        for c in range(M):
            if matrix[a][b][c] == 0:
                temp = True
            result = max(result, matrix[a][b][c])

if temp:
    print(-1)
else:
    print(result-1)
