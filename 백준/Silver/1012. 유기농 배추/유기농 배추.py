import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())


def bfs(i, j, temp_matrix):  # i => 가로길이 M
    queue = deque()
    queue.append([i, j])

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        # print(temp_matrix)
        i, j = queue.popleft()
        for _ in range(4):
            nx = i + dx[_]
            ny = j + dy[_]

            if 0 <= nx < M and 0 <= ny < N:
                if temp_matrix[ny][nx] == 1:
                    temp_matrix[ny][nx] = 0
                    queue.append([nx, ny])
    return


for _ in range(test_case):
    M, N, K = list(map(int, input().split()))
    matrix = [[0] * M for temp in range(N)]
    result = 0

    for temp_k in range(K):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    # print(matrix)
    for temp_m in range(M):
        for temp_n in range(N):
            if matrix[temp_n][temp_m] == 1:
                bfs(temp_m, temp_n, matrix)
                result += 1

    print(result)
