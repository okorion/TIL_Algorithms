import sys

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
dp = [1] * N
dp2 = [1] * N

# print(temp_list)

for i in range(N):
    for j in range(i+1):
        if temp_list[i] > temp_list[j]:
            # dp[i] = dp[j] + 1
            dp[i] = max(dp[i], dp[j] + 1)
        if temp_list[-i-1] > temp_list[-j-1]:
            dp2[-i-1] = max(dp2[-i-1], dp2[-j-1] + 1)

result = [x + y for x, y in zip(dp, dp2)]

print(max(result)-1)
