import sys
input = sys.stdin.readline

N = int(input())

card_price_list = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

# print(card_price_list)
# print(dp)

dp[1] = card_price_list[1]

for i in range(1, N+1):
    for j in range(1, i+1):    # dp[3] => dp[2] + p[1], dp[1] + p[2], dp[0] + p[3]
        dp[i] = max(dp[i-j]+card_price_list[j], dp[i])

print(dp[N])
