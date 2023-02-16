import sys
input = sys.stdin.readline

T = int(input())
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0 for _ in range(90)]

for _ in range(6, 100):
    dp[_] = dp[_-1] + dp[_-5]

for _ in range(T):
    temp = int(input())
    print(dp[temp-1])
