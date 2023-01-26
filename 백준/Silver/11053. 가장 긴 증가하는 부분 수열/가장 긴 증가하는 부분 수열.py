import sys
import copy

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
dp = [1] * N

# print(temp_list)

for i in range(N):
    for j in range(i):
        if temp_list[i] > temp_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
