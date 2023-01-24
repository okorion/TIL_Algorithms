import sys

input = sys.stdin.readline

first_str = list(input().strip())
second_str = list(input().strip())

# print(first_str)
# print(second_str)

two_dimensional_array = [[0] * (len(first_str) + 1) for _ in range(len(second_str) + 1)]

# print(two_dimensional_array)

for i in range(1, len(first_str) + 1):
    for j in range(1, len(second_str) + 1):
        if first_str[i-1] == second_str[j-1]:
            two_dimensional_array[j][i] = two_dimensional_array[j-1][i-1] + 1
        else:
            two_dimensional_array[j][i] = max(two_dimensional_array[j][i-1], two_dimensional_array[j-1][i])

print(two_dimensional_array[-1][-1])
