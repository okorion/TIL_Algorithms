import sys
input = sys.stdin.readline

N, M = map(int, input().split())
temp_list = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

K = int(input())
result = 0

for n in range(1, N+1):
    for m in range(1, M+1):
        dp[n][m] = temp_list[n-1][m-1] + dp[n-1][m] + dp[n][m-1] - dp[n-1][m-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())

    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
