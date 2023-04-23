import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
area_list = [[0] * M for _ in range(N)]

# print(matrix)

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for n in range(N):
    for m in range(M):
        area_list[n][m] += matrix[n][m] * 6

        if matrix[n][m] >= 2:
            area_list[n][m] -= (matrix[n][m] - 1) * 2

        for _ in range(4):
            nx = n + dx[_]
            ny = m + dy[_]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[n][m] >= matrix[nx][ny]:
                    area_list[n][m] -= matrix[nx][ny]
                else:
                    area_list[n][m] -= matrix[n][m]

print(sum(sum(area_list, [])))
