import sys
input = sys.stdin.readline

result = int(input())
cnt = 0
dp = [0] * (result + 1)

for i in range(2, result + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[result])
