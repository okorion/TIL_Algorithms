import sys

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
dp = [1] * N
result_list = []

for i in range(N):
    for j in range(i):
        if temp_list[i] > temp_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

temp = max(dp)

for a in range(-1, -N-1, -1):
    if dp[a] == temp:
        temp -= 1
        result_list.append(temp_list[a])

# print(result_list)
print(max(dp))
print(*reversed(result_list))

# result_list.reverse()
# for i in result_list:
#     print(i, end=' ')
# print(*result_list)
# print(dp)
# print(' '.join([str(a) for a in reversed(result_list)]))
