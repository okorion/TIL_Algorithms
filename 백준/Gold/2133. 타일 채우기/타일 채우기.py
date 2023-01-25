import sys

input = sys.stdin.readline

N = int(input())
dp = [1] + [0] * 31

# print(dp)
for i in range(2, N+1, 2):
    dp[i] = dp[i-2] * 3

    for j in range(0, i-2, 2):
        dp[i] += dp[j] * 2

print(dp[N])
