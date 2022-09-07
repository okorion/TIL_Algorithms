import sys

input = sys.stdin.readline

N = int(input())

temp_list = list(map(int, input().split()))

M = max(temp_list)

for _ in range(len(temp_list)):
    temp_list[_] = temp_list[_] / M * 100

sum_M = sum(temp_list)

result = sum_M / N

print(result)
