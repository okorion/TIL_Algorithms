import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[_] * N for _ in range(1, K+1)]

# print(dp)
for n in range(N):
    for k in range(K):
        if n > 0 and k > 0:
            dp[k][n] = (dp[k-1][n] + dp[k][n-1]) % 1000000000

print(dp[-1][-1])
