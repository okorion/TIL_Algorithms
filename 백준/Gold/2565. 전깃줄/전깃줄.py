import sys

input = sys.stdin.readline

N = int(input())
wire_list = []

for _ in range(N):
    wire_list.append(list(map(int, input().split())))

# print(wire_list)

wire_list.sort(key=lambda x: [x])

# print(wire_list)

dp = [1] * N

for i in range(N):
    for j in range(i):
        if wire_list[i][1] > wire_list[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(N - max(dp))