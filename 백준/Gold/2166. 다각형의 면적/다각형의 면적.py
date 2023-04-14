import sys

input = sys.stdin.readline

N = int(input())
temp_list = []

for _ in range(N):
    temp_list.append(list(map(int, input().split())))

temp_list.append(temp_list[0])

left = 0
right = 0
result = 0

for a, b in temp_list:
    result += right * a
    result -= left * b

    left = a
    right = b

print(round(abs(result/2), 1))
