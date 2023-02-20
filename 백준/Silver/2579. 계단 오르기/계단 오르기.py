import sys
input = sys.stdin.readline

N = int(input())
stair_list = [int(input()) for _ in range(N)]
dp = [0] * N

# print(stair_list)

if len(stair_list) <= 2:
    print(sum(stair_list))

else:
    dp[0] = stair_list[0]
    dp[1] = stair_list[1] + stair_list[0]
    # print(N+1)

    for _ in range(2, N):
        dp[_] = max(dp[_-3] + stair_list[_-1] + stair_list[_], dp[_-2] + stair_list[_])
        # print(_, dp, stair_list, dp[-1])
    print(dp[N-1])
