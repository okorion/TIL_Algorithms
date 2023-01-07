import sys
from collections import deque

input = sys.stdin.readline

N = int(input())    # 처음 아기 상어 크기는 2, 크기만큼 수의 물고기를 먹으면 size up

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().strip().split())))

# print(matrix)

shark_x, shark_y = 0, 0
shark_size = 2
INF = 1e9

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for a in range(N):
    for b in range(N):
        if matrix[a][b] == 9:
            shark_x, shark_y = a, b
            matrix[a][b] = 0


# 현재 위치에서 각 물고기까지의 거리 반환, 지나는 경로마다 값 저장
def go_fish():
    queue = deque()
    queue.append([shark_x, shark_y])
    visited_matrix = [[0] * N for _ in range(N)]
    visited_matrix[shark_x][shark_y] = 1

    while queue:
        p, q = queue.popleft()

        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]

            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] <= shark_size and visited_matrix[nx][ny] == 0:
                    visited_matrix[nx][ny] = visited_matrix[p][q] + 1
                    queue.append([nx, ny])

    return visited_matrix


# 먹을 물고기 찾기
def solve(visited_matrix):
    min_distance = INF
    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if visited_matrix[i][j] != 0 and 1 <= matrix[i][j] < shark_size:
                if visited_matrix[i][j] < min_distance:
                    min_distance = visited_matrix[i][j]
                    x, y = i, j

    if min_distance == INF:
        return False
    else:
        return x, y, min_distance


answer = 0
fish = 0

while True:
    result = solve(go_fish())

    if not result:
        print(answer)
        break
    else:
        answer += result[2] - 1    # visit한 칸은 제외
        shark_x, shark_y = result[0], result[1]
        matrix[shark_x][shark_y] = 0
        fish += 1

    if fish == shark_size:
        shark_size += 1
        fish = 0
