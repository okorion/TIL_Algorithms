import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [[0 for _ in range(M)] for k in range(N)]
matrix = []

# print(visited)

for _ in range(N):
    matrix.append(list(map(int, input().split())))

# print(matrix)

# for i in range(M):
#     for j in range(N):
#


def dfs(i, j):
    queue = deque()
    queue.append([i, j])
    count = 1
    matrix[j][i] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        p, q = queue.popleft()
        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]

            if 0 <= nx < M and 0 <= ny < N:
                if matrix[ny][nx] == 1:
                    count += 1
                    matrix[ny][nx] = 0
                    queue.append([nx, ny])

    return count


result = 0
max_val = 0

for a in range(M):
    for b in range(N):
        if matrix[b][a] == 1:
            temp = dfs(a, b)
            if temp > max_val:
                max_val = temp
            result += 1

print(result)
print(max_val)
