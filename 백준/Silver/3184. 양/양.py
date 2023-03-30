import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(R)]

# print(matrix)
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
visited = [[0] * C for _ in range(R)]
queue = deque()
result_sheep = 0
result_wolf = 0


def bfs(y, x, val):
    global result_sheep
    global result_wolf

    sheep_cnt = 0
    wolf_cnt = 0

    if val == 'v':
        wolf_cnt += 1
    elif val == 'o':
        sheep_cnt += 1

    if visited[y][x] == 1:
        return

    elif visited[y][x] == 0:
        queue.append([y, x])
        visited[y][x] = 1

        while queue:
            a, b = queue.popleft()

            for _ in range(4):
                nx = dx[_] + b
                ny = dy[_] + a

                if 0 <= ny < R and 0 <= nx < C:
                    if matrix[ny][nx] == '.' and visited[ny][nx] == 0:
                        queue.append([ny, nx])
                        visited[ny][nx] = 1

                    elif matrix[ny][nx] == 'o' and visited[ny][nx] == 0:
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        sheep_cnt += 1

                    elif matrix[ny][nx] == 'v' and visited[ny][nx] == 0:
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        wolf_cnt += 1

    # print(sheep_cnt, wolf_cnt)
    # print(visited)

    if sheep_cnt > wolf_cnt:
        result_sheep += sheep_cnt

    else:
        result_wolf += wolf_cnt


for i in range(R):
    for j in range(C):
        if matrix[i][j] == '.' or matrix[i][j] == 'o' or matrix[i][j] == 'v':
            bfs(i, j, matrix[i][j])

print(result_sheep, result_wolf)
