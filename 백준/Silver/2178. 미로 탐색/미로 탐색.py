from collections import deque

N, M = map(int, input().split())
matrix = []
result_list = []

for _ in range(N):
    matrix.append(list(map(int, input().strip())))

# matrix[N][M] 에 도착했을 때 지나는 칸 수 return 함수


def bfs_miro(i, j):
    queue = deque()
    queue.append([i, j])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        i, j = queue.popleft()

        for _ in range(4):
            nx = i + dx[_]
            ny = j + dy[_]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = matrix[i][j] + 1
                    queue.append([nx, ny])

    return matrix[N-1][M-1]


print(bfs_miro(0, 0))
