import sys
from collections import deque
sys.setrecursionlimit(10000)

input = sys.stdin.readline

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, -1, 0, 1, 1, -1, 1, -1]


def bfs(i, j):            # i => 4, j => 5
    queue = deque()
    queue.append([i, j])
    visited_list[i][j] = 1

    while queue:
        a, b = queue.popleft()

        for _ in range(8):
            nx = a + dx[_]
            ny = b + dy[_]

            if 0 <= nx < M and 0 <= ny < N:
                if visited_list[nx][ny] == 0 and matrix[nx][ny] == 1:
                    visited_list[nx][ny] = 1
                    queue.append([nx, ny])

    return True


while True:
    N, M = map(int, input().split())
    matrix = [[] for _ in range(M)]
    visited_list = [[0]*N for _ in range(M)]
    cnt = 0
    
    if N == 0 and M == 0:
        break
        
    for _ in range(M):
        matrix[_] = list(map(int, input().split()))

    for p in range(M):  # N => 5 , M => 4
        for q in range(N):
            if matrix[p][q] == 1 and visited_list[p][q] == 0:
                if bfs(p, q):
                    cnt += 1

    print(cnt)
