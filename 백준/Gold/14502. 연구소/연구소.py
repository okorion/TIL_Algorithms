import copy
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lab_matrix = [list(map(int, input().split())) for _ in range(N)]
max_result = 0

# print(lab_matrix)


def bfs():
    global max_result

    virus = deque()
    temp_lab_matrix = copy.deepcopy(lab_matrix)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    result = 0

    for i in range(N):
        for j in range(M):
            if lab_matrix[i][j] == 2:
                virus.append([i, j])

    while virus:
        x, y = virus.pop()

        for _ in range(4):
            nx = dx[_] + x
            ny = dy[_] + y

            if 0 <= nx < N and 0 <= ny < M:
                if temp_lab_matrix[nx][ny] == 0:
                    temp_lab_matrix[nx][ny] = 2
                    virus.append([nx, ny])

    for i in range(N):
        for j in range(M):
            if temp_lab_matrix[i][j] == 0:
                result += 1

    max_result = max(max_result, result)


def make_walls(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab_matrix[i][j] == 0:
                lab_matrix[i][j] = 1
                make_walls(count+1)
                lab_matrix[i][j] = 0


make_walls(0)

print(max_result)
