import sys
input = sys.stdin.readline

N = int(input())
result = 0

for _ in range(8, -1, -1):
    if N <= 9:
        result += N
        break

    if N // (10 ** _):
        # print(N, N - (10 ** _) + 1, (_ + 1))
        result += (N - (10 ** _) + 1) * (_ + 1)
        # print('result', result)
        N -= N - (10 ** _) + 1
        # print('N', N)

print(result)
