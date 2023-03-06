import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
# matrix = [list(input().rstrip()) for _ in range(R)]
matrix = [list(map(lambda a: ord(a) - 65, input().rstrip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
temp_list = [False] * 26
temp_list[matrix[0][0]] = True
result = 0

# print(matrix)


def dfs(x, y, cnt):
    global result

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    visited[x][y] = 1
    temp_list[matrix[x][y]] = True

    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]

        if 0 <= nx < R and 0 <= ny < C:
            if visited[nx][ny] == 0 and not temp_list[matrix[nx][ny]]:
                # print([a, b], [nx, ny])
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0
                temp_list[matrix[nx][ny]] = False

    result = max(result, cnt)

    return


dfs(0, 0, 1)
print(result)
