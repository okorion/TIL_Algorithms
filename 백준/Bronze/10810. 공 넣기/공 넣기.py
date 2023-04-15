import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp_list = [0] * N

for _ in range(M):
    start, end, k = map(int, input().split())

    for t in range(start - 1, end):
        temp_list[t] = k

print(*temp_list)
