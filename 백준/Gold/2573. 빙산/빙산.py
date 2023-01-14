import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = deque()
day = 0
check = False


def bfs(a, b):
    queue.append([a, b])
    visited[a][b] = 1
    
    while queue:
        x, y = queue.popleft()

        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]

            if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx, ny])
            elif graph[nx][ny] == 0:
                count[x][y] += 1
    return 1


while True:
    visited = [[0] * M for _ in range(N)]
    count = [[0] * M for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and visited[i][j] == 0:
                result.append(bfs(i, j))
                # print(bfs(i, j))
                # print(result)
                # print(graph)

    for i in range(N):
        for j in range(M):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(result) == 0:
        break

    if len(result) >= 2:
        check = True
        break

    day += 1

if check:
    print(day)
else:
    print(0)