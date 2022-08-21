import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
dp[1], dp[2] = 1, 1

cnt_re = 0
cnt_memo = 0
cnt_tab = 0


def recursion(n):           # 재귀함수
    global cnt_re
    if n == 1 or n == 2:
        cnt_re += 1
        return 1
    elif n >= 3:
        return recursion(n-1) + recursion(n-2)


# print(recursion(N), len(cnt_re))


def memoization(n):           # 메모이제이션 (하향식)
    global cnt_memo
    if dp[n] == 0:
        dp[n] = memoization(n-1) + memoization(n-2)
        cnt_memo += 1
    return dp[n]


# print(memoization(N), len(cnt_memo))


def tabulation(n):             # 타뷸레이션 (상향식)
    global cnt_tab
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt_tab += 1
    return dp[n]


# print(tabulation(N), len(cnt_tab))

recursion(N)
tabulation(N)

print(cnt_re, cnt_tab)
