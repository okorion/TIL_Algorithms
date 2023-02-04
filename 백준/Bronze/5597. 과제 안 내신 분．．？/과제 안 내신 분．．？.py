import sys

input = sys.stdin.readline

temp_list = []

for _ in range(28):
    a = int(input())

    temp_list.append(a)

result = []

for _ in range(1, 31):
    if _ not in temp_list:
        result.append(_)

print(min(result))
print(max(result))
