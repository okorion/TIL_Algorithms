import sys

input = sys.stdin.readline

N = int(input())
max_value = 0
result = ""
temp_list = []

for _ in range(N):
    name, num = input().split()

    temp_list.append([str(name), int(num)])

temp_list.sort(reverse=True)

for name, num in temp_list:
    if num >= max_value:
        max_value = num
        result = name

print(result)
