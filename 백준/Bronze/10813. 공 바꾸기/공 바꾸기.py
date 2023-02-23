import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

temp_list = list(range(1, N+1))

# print(temp_list)

for _ in range(M):
    a, b = map(int, input().split())
    temp = copy.deepcopy(temp_list[b-1])

    temp_list[b-1] = temp_list[a-1]
    temp_list[a-1] = temp

print(*temp_list)
