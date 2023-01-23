import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())
triangle = []
dp = [[0] * N for _ in range(N)]

for _ in range(N):
    triangle.append(list(map(int, input().split())))

dp[0][0] = triangle[0][0]

# print(dp)
# print(triangle)

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        else:
            dp[i][j] = triangle[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[N-1]))
