import sys
import copy

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
dp = [1] * N
result_list = copy.deepcopy(temp_list)

for i in range(N):
    for j in range(i):
        if temp_list[i] > temp_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            result_list[i] = max(result_list[i], temp_list[i] + result_list[j])

# print(dp)
# print(temp_list)
# print(result_list)
print(max(result_list))
