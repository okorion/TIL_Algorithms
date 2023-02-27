import sys
input = sys.stdin.readline

n = int(input())

dp = [[0, []] for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = [1]

for _ in range(2, n + 1):
    dp[_][0] = dp[_-1][0] + 1    #카운트 + 1
    dp[_][1] = dp[_-1][1] + [_]    #흔적 남기기

    if _ % 3 == 0 and dp[_ // 3][0] + 1 < dp[_][0]:
        dp[_][0] = dp[_ // 3][0] + 1
        dp[_][1] = dp[_ // 3][1] + [_]

    if _ % 2 == 0 and dp[_ // 2][0] + 1 < dp[_][0]:
        dp[_][0] = dp[_ // 2][0] + 1
        dp[_][1] = dp[_ // 2][1] + [_]


print(dp[n][0])
print(*reversed(dp[n][1]))
