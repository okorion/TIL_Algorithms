import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0]*2 for t in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j, k):
    queue = deque()
    queue.append([i, j, k])

    while queue:
        p, q, r = queue.popleft()

        if p == (N-1) and q == (M-1):
            return visited[p][q][r]

        for _ in range(4):
            nx = p + dx[_]
            ny = q + dy[_]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1 and r == 0:
                    visited[nx][ny][1] += visited[p][q][0] + 1
                    queue.append([nx, ny, 1])

                if matrix[nx][ny] == 0 and visited[nx][ny][r] == 0:
                    visited[nx][ny][r] = visited[p][q][r] + 1
                    queue.append([nx, ny, r])

    return -1


print(bfs(0, 0, 0))
