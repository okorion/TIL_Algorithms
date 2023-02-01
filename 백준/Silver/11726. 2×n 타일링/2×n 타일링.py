import sys

input = sys.stdin.readline

N = int(input())

result = 1
dp = [1, 1]
n = 3

while True:
    if n == N + 2:
        print(dp[n-2] % 10007)
        break

    else:
        dp.append(dp[n-3] + dp[n-2])
        n += 1

