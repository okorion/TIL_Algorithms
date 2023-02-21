import sys
input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))

for _ in range(1, N):
    temp_list[_] = max(temp_list[_], temp_list[_ - 1] + temp_list[_])

print(max(temp_list))
