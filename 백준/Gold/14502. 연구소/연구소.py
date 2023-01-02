import copy
import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
matrix = []
virus_list = []
max_value = 0

for _ in range(N):
    matrix.append(list(map(int, input().strip().split())))

for _ in range(N*M):
    i = _ // M
    j = _ % M
    if matrix[i][j] == 2:
        virus_list.append([i, j])


# 벽 만들기
def build_wall(start, count):
    global max_value
    if count == 3:
        temp_matrix = copy.deepcopy(matrix)
        for _ in range(len(virus_list)):
            p, q = virus_list[_]
            spread_virus(p, q, temp_matrix)
        result = sum(k.count(0) for k in temp_matrix)
        max_value = max(max_value, result)

        return True
    else:
        for _ in range(start, N*M):
            a = _ // M
            b = _ % M
            if matrix[a][b] == 0:
                matrix[a][b] = 1
                build_wall(start, count+1)
                matrix[a][b] = 0


# 바이러스 확산
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def spread_virus(x, y, temp_matrix):
    if temp_matrix[x][y] == 2:
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < N and 0 <= ny < M:
                if temp_matrix[nx][ny] == 0:
                    temp_matrix[nx][ny] = 2
                    spread_virus(nx, ny, temp_matrix)


build_wall(0, 0)
print(max_value)
