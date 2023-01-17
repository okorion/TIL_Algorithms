import sys

input = sys.stdin.readline

temp_list = []
temp_list.append(input().split('-'))

# print(temp_list)

for _ in range(len(temp_list[0])):
    if '+' in temp_list[0][_]:
        temp_list[0][_] = sum(map(int, temp_list[0][_].split('+')))
    else:
        temp_list[0][_] = int(temp_list[0][_])

result = temp_list[0][0]

for _ in range(1, len(temp_list[0])):
    result -= temp_list[0][_]

print(result)
