import sys

input = sys.stdin.readline

N = int(input())

dp = [3, 5]

if N == 1:
    print(1)
elif N == 2:
    print(3)
elif N == 3:
    print(5)
else:
    for _ in range(2, N - 1):
        dp.append(3 * dp[_ - 2] + (dp[_ - 1] - dp[_ - 2]))

    print(dp[-1] % 10007)
