import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = []
dp = [0] * (k+1)
dp[0] = 1

for _ in range(n):
    coin_list.append(int(input()))

# print(coin_list)

for c in coin_list:
    for temp in range(k+1):
        if temp - c >= 0:
            dp[temp] += dp[temp-c]

print(dp[k])
