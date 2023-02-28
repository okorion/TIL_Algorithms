import sys
input = sys.stdin.readline

A_str = [""] + list(input().rstrip())
B_str = [""] + list(input().rstrip())
dp = [[""] * len(B_str) for _ in range(len(A_str))]


for i in range(1, len(A_str)):
    for j in range(1, len(B_str)):
        if A_str[i] == B_str[j]:
            dp[i][j] = dp[i-1][j-1] + A_str[i]     # A_str[i] or B_str[j]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]


result = dp[-1][-1]
print(len(result), result, sep='\n')
