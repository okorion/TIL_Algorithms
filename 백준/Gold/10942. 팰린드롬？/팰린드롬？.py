import sys
input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if temp_list[i] == temp_list[i+1]:
        dp[i][i+1] = 1

for i in range(2, N):    # j는 start, i는 end 까지의 거리
    for j in range(N - i):
        if temp_list[j] == temp_list[j + i] and dp[j + 1][j + i - 1] == 1:
            dp[j][j + i] = 1

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    print(dp[a-1][b-1])

