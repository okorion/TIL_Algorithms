import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

M, N = map(int, input().split())
matrix = []

for _ in range(M):
    matrix.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(M)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


def dfs(x, y):    # *Top-Down (Memoization)  <-> Bottom-Up (Tabulation)
    if x == M-1 and y == N-1:    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
        return 1

    if dp[x][y] != -1:    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[x][y] > matrix[nx][ny]:
                ways += dfs(nx, ny)

    dp[x][y] = ways

    return dp[x][y]


print(dfs(0, 0))
