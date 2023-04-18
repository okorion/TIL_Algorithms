import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp_list = list(range(1, N + 1))

for m in range(M):
    i, j, k = map(int, input().split())

    temp_list = temp_list[0:i - 1] + temp_list[k - 1:j] + temp_list[i - 1:k - 1] + temp_list[j:N]

print(*temp_list)
