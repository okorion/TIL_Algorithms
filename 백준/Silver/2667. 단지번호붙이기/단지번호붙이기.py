from collections import deque

N = int(input())
matrix = []
result_list = []

for _ in range(N):
    matrix.append(list(map(int, input().strip())))


def bfs_home(i, j):
    matrix[i][j] = 0
    count = 1
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    queue = deque()
    queue.append([i, j])

    while queue:
        i, j = queue.popleft()
        for _ in range(4):
            nx = i + dx[_]
            ny = j + dy[_]

            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1:
                    queue.append([nx, ny])
                    count += 1
                    matrix[nx][ny] = 0

    return count


for _ in range(N*N):
    a = _ // N
    b = _ % N
    if matrix[a][b] == 1:
        result_list.append(bfs_home(a, b))

result_list.sort()

print(len(result_list))
for _ in range(len(result_list)):
    print(result_list[_])
