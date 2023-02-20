import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 12

dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(4, 12):
    dp[_] = dp[_-3] + dp[_-2] + dp[_-1]

for _ in range(T):
    t = int(input())
    print(dp[t])