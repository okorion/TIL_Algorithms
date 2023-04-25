import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * N
np = []

for _ in range(N):
    np.append(int(input()))

for _ in range(N):
    if _ == 0:
        dp[_] = np[_]
    elif _ == 1:
        dp[_] = np[0] + np[1]
    elif _ == 2:
        dp[_] = max(np[0] + np[2], np[1] + np[2], dp[1])
    else:
        dp[_] = max(dp[_ - 2] + np[_], dp[_ - 3] + np[_ - 1] + np[_], dp[_ - 1])

print(max(dp))
