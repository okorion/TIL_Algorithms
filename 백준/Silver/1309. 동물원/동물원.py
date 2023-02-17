import sys
input = sys.stdin.readline

N = int(input())
dp = [1] * (N + 1)
mod = 9901

# print(dp)

dp[0] = 1

for _ in range(1, N+1):
    dp[_] = (2 * dp[_-1] + dp[_-2]) % mod

print(dp[N])
